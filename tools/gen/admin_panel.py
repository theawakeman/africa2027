# -*- coding: utf-8 -*-
"""Panel de edición de puntos de interés (/admin/) para África 2027.

Página estática que habla directamente con la API de contenidos de GitHub
(usando un token personal que el propio usuario pega y que se guarda SOLO en
su navegador) para leer y escribir content/pois/<slug>.json. No pasa por
ningún backend propio: es un cliente puro que hace fetch() a api.github.com.
"""
import json

REPO = "theawakeman/africa2027"
BRANCH = "main"

ADMIN_CSS = """
:root{color-scheme:light;--a-teal:#1E7A8A;--a-head:#16324F;--a-ink:#1c2b34;--a-ink-soft:#5b6b74;--a-surface:#fff;--a-surface2:#f4f7f8;--a-line:#e1e8ea;--a-red:#B43A3A;--a-green:#2E7D32;--a-amber:#C47F17}
*{box-sizing:border-box}
body{font-family:"Archivo",sans-serif;background:var(--a-surface2);color:var(--a-ink);margin:0}
.wrap{max-width:920px;margin:0 auto;padding:18px 16px 60px}
h1{font-size:22px;color:var(--a-head);margin:18px 0 4px}
h2{font-size:17px;color:var(--a-head);margin:26px 0 10px}
p.lead{color:var(--a-ink-soft);font-size:14px;margin:0 0 18px}
.card{background:var(--a-surface);border:1px solid var(--a-line);border-radius:10px;padding:16px;margin-bottom:16px}
label{display:block;font-size:12.5px;font-weight:700;color:var(--a-ink-soft);margin:12px 0 4px}
label:first-child{margin-top:0}
input[type=text],input[type=number],input[type=url],textarea,select{width:100%;padding:9px 10px;border:1px solid var(--a-line);border-radius:7px;font-size:14px;font-family:inherit;background:#fff;color:#1c2b34;color-scheme:light}
textarea{min-height:70px;resize:vertical}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.btn{display:inline-block;background:var(--a-teal);color:#fff;border:none;border-radius:8px;padding:9px 18px;font-size:14px;font-weight:700;cursor:pointer;font-family:inherit}
.btn.ghost{background:transparent;color:var(--a-teal);border:1px solid var(--a-teal)}
.btn.danger{background:var(--a-red)}
.btn:disabled{opacity:.5;cursor:default}
.toolbar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:10px 0 18px}
.poi-list{display:flex;flex-direction:column;gap:8px}
.poi-row{display:flex;align-items:center;gap:12px;background:var(--a-surface);border:1px solid var(--a-line);border-radius:9px;padding:8px 12px}
.poi-row img{width:56px;height:56px;object-fit:cover;border-radius:6px;background:var(--a-surface2);flex-shrink:0}
.poi-row .meta{flex:1;min-width:0}
.poi-row .meta b{display:block;font-size:14.5px;color:var(--a-head)}
.poi-row .meta span{font-size:12.5px;color:var(--a-ink-soft)}
.poi-row .acts{display:flex;gap:6px;flex-shrink:0}
.poi-row .acts button{border:none;background:var(--a-surface2);border-radius:6px;padding:6px 10px;font-size:12.5px;cursor:pointer;font-family:inherit;color:#1c2b34}
#msg{margin:12px 0;padding:10px 14px;border-radius:8px;font-size:14px;display:none}
#msg.ok{display:block;background:#e6f4ea;color:var(--a-green)}
#msg.err{display:block;background:#fbe9e7;color:var(--a-red)}
#msg.info{display:block;background:#eef6f8;color:var(--a-teal)}
.hint{font-size:12px;color:var(--a-ink-soft);margin-top:4px}
[hidden]{display:none!important}
"""

# Placeholders __COUNTRIES_JSON__, __REPO__, __BRANCH__ se sustituyen al generar la página.
ADMIN_JS = r"""
const REPO = "__REPO__";
const BRANCH = "__BRANCH__";
const SITE_URL = "https://theawakeman.github.io/africa2027/";
const COUNTRIES = __COUNTRIES_JSON__;
const API = "https://api.github.com/repos/" + REPO;

function tok(){ return localStorage.getItem("a27_gh_pat") || ""; }
function authHeaders(){ return {"Authorization": "Bearer " + tok(), "Accept": "application/vnd.github+json"}; }

function utf8ToB64(str){
  const bytes = new TextEncoder().encode(str);
  let bin = "";
  bytes.forEach(b => bin += String.fromCharCode(b));
  return btoa(bin);
}
function b64ToUtf8(b64){
  const bin = atob(b64.replace(/\n/g, ""));
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return new TextDecoder().decode(bytes);
}

function msg(text, kind){
  const el = document.getElementById("msg");
  el.textContent = text;
  el.className = kind || "info";
  if (!text) el.className = "";
}

let currentSlug = null;
let currentPois = null;   // array en memoria
let currentSha = null;    // sha del archivo en GitHub, para poder guardar
let editingIndex = null;  // índice dentro de currentPois que se está editando, o null = punto nuevo

function imgSrc(img){
  if (!img) return "";
  return img.indexOf("http") === 0 ? img : SITE_URL + img;
}

function fillCountrySelect(){
  const sel = document.getElementById("countrySelect");
  sel.innerHTML = '<option value="">— elegir país —</option>' +
    COUNTRIES.map(c => `<option value="${c.slug}">${c.name}</option>`).join("");
}

async function loadCountry(slug){
  currentSlug = slug;
  currentPois = null; currentSha = null; editingIndex = null;
  document.getElementById("poiList").innerHTML = "";
  document.getElementById("formCard").hidden = true;
  if (!slug) return;
  msg("Cargando puntos de " + slug + "…", "info");
  try {
    const res = await fetch(`${API}/contents/content/pois/${slug}.json?ref=${BRANCH}`, {headers: authHeaders()});
    if (!res.ok) throw new Error("GitHub respondió " + res.status + " — revisa el token o el nombre del país.");
    const data = await res.json();
    currentSha = data.sha;
    currentPois = JSON.parse(b64ToUtf8(data.content));
    renderPoiList();
    msg("", "");
  } catch (e){
    msg("Error al cargar: " + e.message, "err");
  }
}

function renderPoiList(){
  const list = document.getElementById("poiList");
  if (!currentPois || !currentPois.length){ list.innerHTML = "<p class='hint'>Este país todavía no tiene puntos.</p>"; return; }
  list.innerHTML = currentPois.map((p, i) => `
    <div class="poi-row">
      <img src="${imgSrc(p.img)}" alt="" loading="lazy" onerror="this.style.visibility='hidden'">
      <div class="meta"><b>${p.name || "(sin nombre)"}</b><span>${p.cat || ""}${p.prio ? " · " + p.prio : ""}</span></div>
      <div class="acts">
        <button onclick="openEdit(${i})">Editar</button>
        <button onclick="deletePoi(${i})">Borrar</button>
      </div>
    </div>`).join("");
}

function openEdit(index){
  editingIndex = index;
  const p = index === null ? {} : currentPois[index];
  document.getElementById("formTitle").textContent = index === null ? "Añadir punto nuevo" : "Editar punto";
  document.getElementById("f_name").value = p.name || "";
  document.getElementById("f_cat").value = p.cat || "";
  document.getElementById("f_prio").value = p.prio || "Recomendable";
  document.getElementById("f_color").value = p.color || "ambar";
  document.getElementById("f_dog").value = p.dog || "";
  document.getElementById("f_dog_note").value = p.dog_note || "";
  document.getElementById("f_time").value = p.time || "";
  document.getElementById("f_lat").value = p.lat ?? "";
  document.getElementById("f_lon").value = p.lon ?? "";
  document.getElementById("f_desc").value = p.desc || "";
  document.getElementById("f_img").value = p.img || "";
  document.getElementById("f_credit").value = p.credit || "";
  document.getElementById("f_source").value = p.source || "";
  document.getElementById("f_icon").value = p.icon || "";
  document.getElementById("formCard").hidden = false;
  document.getElementById("formCard").scrollIntoView({behavior:"smooth", block:"start"});
}

function closeForm(){
  document.getElementById("formCard").hidden = true;
  editingIndex = null;
}

function deletePoi(index){
  const p = currentPois[index];
  if (!confirm(`¿Borrar "${p.name}"? Esto se sube directamente a GitHub.`)) return;
  currentPois.splice(index, 1);
  savePois(`Borrar POI: ${p.name} (${currentSlug})`);
}

function nextN(){
  return currentPois.reduce((m, p) => Math.max(m, p.n || 0), 0) + 1;
}

function submitForm(ev){
  ev.preventDefault();
  const lat = parseFloat(document.getElementById("f_lat").value);
  const lon = parseFloat(document.getElementById("f_lon").value);
  const name = document.getElementById("f_name").value.trim();
  if (!name || isNaN(lat) || isNaN(lon)){
    msg("Nombre, latitud y longitud son obligatorios.", "err");
    return;
  }
  const poi = {
    n: editingIndex === null ? nextN() : currentPois[editingIndex].n,
    name, lat, lon,
    cat: document.getElementById("f_cat").value.trim(),
    prio: document.getElementById("f_prio").value,
    color: document.getElementById("f_color").value,
    dog: document.getElementById("f_dog").value.trim(),
    dog_note: document.getElementById("f_dog_note").value.trim(),
    time: document.getElementById("f_time").value.trim(),
    desc: document.getElementById("f_desc").value.trim(),
    img: document.getElementById("f_img").value.trim(),
    credit: document.getElementById("f_credit").value.trim(),
    source: document.getElementById("f_source").value.trim(),
    icon: document.getElementById("f_icon").value.trim(),
  };
  if (editingIndex === null) currentPois.push(poi);
  else currentPois[editingIndex] = poi;
  savePois(`${editingIndex === null ? "Añadir" : "Editar"} POI: ${name} (${currentSlug})`);
}

async function savePois(commitMessage){
  msg("Guardando en GitHub…", "info");
  try {
    const body = {
      message: commitMessage,
      content: utf8ToB64(JSON.stringify(currentPois, null, 2) + "\n"),
      sha: currentSha,
      branch: BRANCH,
    };
    const res = await fetch(`${API}/contents/content/pois/${currentSlug}.json`, {
      method: "PUT", headers: {...authHeaders(), "Content-Type": "application/json"}, body: JSON.stringify(body),
    });
    if (!res.ok){
      const t = await res.text();
      throw new Error("GitHub respondió " + res.status + ": " + t.slice(0, 200));
    }
    const data = await res.json();
    currentSha = data.content.sha;
    renderPoiList();
    closeForm();
    msg("Guardado. El sitio se reconstruye solo en 1-2 minutos.", "ok");
  } catch (e){
    msg("Error al guardar: " + e.message, "err");
  }
}

function saveToken(){
  const v = document.getElementById("tokenInput").value.trim();
  if (!v) return;
  localStorage.setItem("a27_gh_pat", v);
  showApp();
}
function forgetToken(){
  localStorage.removeItem("a27_gh_pat");
  showApp();
}
function showApp(){
  const has = !!tok();
  document.getElementById("tokenBox").hidden = has;
  document.getElementById("appBox").hidden = !has;
}

document.addEventListener("DOMContentLoaded", () => {
  fillCountrySelect();
  showApp();
  document.getElementById("countrySelect").addEventListener("change", e => loadCountry(e.target.value));
  document.getElementById("poiForm").addEventListener("submit", submitForm);
  document.getElementById("saveTokenBtn").addEventListener("click", saveToken);
  document.getElementById("forgetTokenBtn").addEventListener("click", forgetToken);
  document.getElementById("addBtn").addEventListener("click", () => openEdit(null));
  document.getElementById("cancelBtn").addEventListener("click", closeForm);
});
"""


def render_admin(countries_for_admin):
    """countries_for_admin: lista de dicts {slug, name} — solo países con content/pois/<slug>.json."""
    countries_json = json.dumps(countries_for_admin, ensure_ascii=False)
    js = (ADMIN_JS.replace("__REPO__", REPO)
                  .replace("__BRANCH__", BRANCH)
                  .replace("__COUNTRIES_JSON__", countries_json))
    body = """<div class="wrap">
<h1>Panel de edición · puntos de interés</h1>
<p class="lead">Añade, edita o borra puntos de las fichas de país. Los cambios se guardan directamente en GitHub y el sitio se reconstruye y publica solo en 1-2 minutos.</p>

<div id="msg"></div>

<div class="card" id="tokenBox">
  <h2 style="margin-top:0">Token de acceso</h2>
  <p class="hint">Hace falta un token personal de GitHub para poder guardar cambios. Crea uno en
    <a href="https://github.com/settings/tokens?type=beta" target="_blank" rel="noopener">github.com/settings/tokens</a> →
    "Generate new token" (fine-grained) → repositorio <code>theawakeman/africa2027</code> → permiso
    "Contents: Read and write". El token se guarda solo en este navegador, nunca se sube a ningún sitio.</p>
  <label for="tokenInput">Pegar token</label>
  <input type="text" id="tokenInput" placeholder="github_pat_...">
  <div class="toolbar"><button class="btn" id="saveTokenBtn">Guardar token</button></div>
</div>

<div id="appBox" hidden>
  <div class="toolbar">
    <label style="margin:0;flex:1"><span style="display:block;margin-bottom:4px">País</span>
      <select id="countrySelect"></select>
    </label>
    <button class="btn ghost" id="forgetTokenBtn" style="align-self:flex-end">Olvidar token</button>
  </div>

  <div class="toolbar">
    <button class="btn" id="addBtn">+ Añadir punto</button>
  </div>

  <div class="poi-list" id="poiList"></div>

  <div class="card" id="formCard" hidden>
    <h2 id="formTitle" style="margin-top:0">Punto</h2>
    <form id="poiForm">
      <label for="f_name">Nombre exacto</label>
      <input type="text" id="f_name" required>

      <div class="row2">
        <div><label for="f_cat">Categoría</label><input type="text" id="f_cat" placeholder="p. ej. Naturaleza y cultura"></div>
        <div><label for="f_prio">Prioridad</label>
          <select id="f_prio">
            <option>Imprescindible</option><option>Muy recomendable</option>
            <option>Recomendable</option><option>Opcional</option>
          </select>
        </div>
      </div>

      <div class="row2">
        <div><label for="f_lat">Latitud</label><input type="number" step="0.00001" id="f_lat" required></div>
        <div><label for="f_lon">Longitud</label><input type="number" step="0.00001" id="f_lon" required></div>
      </div>

      <label for="f_desc">Descripción</label>
      <textarea id="f_desc"></textarea>

      <label for="f_img">Foto (URL completa — Wikimedia Commons, o cualquier imagen pública)</label>
      <input type="url" id="f_img" placeholder="https://commons.wikimedia.org/wiki/Special:FilePath/...">
      <p class="hint">De momento el panel no sube archivos de foto directamente: pega la URL de una imagen ya publicada (Wikimedia Commons funciona bien — busca el sitio en commons.wikimedia.org y usa "Special:FilePath/nombre.jpg?width=900").</p>

      <div class="row2">
        <div><label for="f_credit">Crédito de la foto</label><input type="text" id="f_credit"></div>
        <div><label for="f_source">Fuente (URL)</label><input type="url" id="f_source"></div>
      </div>

      <div class="row2">
        <div><label for="f_dog">Perro (estado)</label><input type="text" id="f_dog" placeholder="p. ej. permitido con condiciones"></div>
        <div><label for="f_dog_note">Nota sobre el perro</label><input type="text" id="f_dog_note"></div>
      </div>

      <div class="row2">
        <div><label for="f_color">Color (capa My Maps)</label>
          <select id="f_color">
            <option value="turquesa">Turquesa</option><option value="verde">Verde</option>
            <option value="marron">Marrón</option><option value="naranja">Naranja</option>
            <option value="morado">Morado</option><option value="azul">Azul</option>
            <option value="gris">Gris</option><option value="ambar">Ámbar</option>
          </select>
        </div>
        <div><label for="f_time">Tiempo estimado</label><input type="text" id="f_time" placeholder="p. ej. 1 día"></div>
      </div>

      <label for="f_icon">Icono (solo descriptivo, para tu propia referencia)</label>
      <input type="text" id="f_icon" placeholder="p. ej. árbol / fauna">

      <div class="toolbar">
        <button class="btn" type="submit">Guardar</button>
        <button class="btn ghost" type="button" id="cancelBtn">Cancelar</button>
      </div>
    </form>
  </div>
</div>
</div>
<script>""" + js + "</script>"
    return body
