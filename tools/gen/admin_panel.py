# -*- coding: utf-8 -*-
"""Panel de edición (/admin/) para África 2027: puntos de interés (Fase 1) y
resto de la ficha de país — hero, chips, historia, logística, fuentes y
secciones personalizadas (Fase 2).

Página estática que habla directamente con la API de contenidos de GitHub
(usando un token personal que el propio usuario pega y que se guarda SOLO en
su navegador) para leer y escribir content/pois/<slug>.json y
content/ficha/<slug>.json. No pasa por ningún backend propio: es un cliente
puro que hace fetch() a api.github.com.
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
.tabs{display:flex;gap:0;margin:4px 0 18px;border-bottom:1px solid var(--a-line)}
.tab-btn{background:none;border:none;padding:10px 4px;margin-right:22px;font-size:14.5px;font-weight:700;color:var(--a-ink-soft);cursor:pointer;font-family:inherit;border-bottom:2px solid transparent}
.tab-btn.active{color:var(--a-teal);border-bottom-color:var(--a-teal)}
.rep-item{padding:12px 0;border-top:1px solid var(--a-line)}
.rep-item:first-of-type{border-top:none}
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

let fichaSha = null;      // sha de content/ficha/<slug>.json
let fichaWorking = {};    // copia de trabajo de la ficha (repeaters ya convertidos a objetos)

// -------- Fase 2: resto de la ficha (hero, chips, historia, logística, fuentes, secciones) --------

const SIMPLE_FIELDS = [
  {name:"hero_img", label:"Foto de portada (URL de imagen — Wikimedia Commons u otra pública)", ph:"https://commons.wikimedia.org/wiki/Special:FilePath/..."},
  {name:"hero_credit", label:"Crédito de la foto de portada"},
  {name:"historia_resumen", label:"Resumen de historia (párrafo introductorio de la ficha)", ta:true},
  {name:"notice", label:"Aviso operativo (aparece justo bajo la cabecera)", ta:true},
  {name:"emergency", label:"Teléfonos de emergencia", ta:true},
  {name:"sources_note", label:"Nota sobre las fuentes", ta:true},
  {name:"matrix_note", label:"Nota de consistencia de la matriz de puntos", ta:true},
];

const REPEATER_DEFS = {
  chips: {label:"Chips de cabecera", hint:"Las etiquetas cortas que aparecen bajo el título de la ficha (corredor, ritmo, seguridad...).",
    fields:[{name:"label", label:"Etiqueta", ph:"p. ej. CORREDOR"}, {name:"value", label:"Valor", ph:"p. ej. Diama → Kalifourou"}],
    fromArr:a=>({label:a?.[0]??"", value:a?.[1]??""}), toArr:o=>[o.label||"", o.value||""]},
  historia_secciones: {label:"Secciones de la historia", hint:"Los bloques de la página «Historia de …» (título + texto de cada época).",
    fields:[{name:"title", label:"Título"}, {name:"text", label:"Texto", ta:true}],
    fromArr:a=>({title:a?.[0]??"", text:a?.[1]??""}), toArr:o=>[o.title||"", o.text||""]},
  historia_fuentes: {label:"Fuentes de la historia", hint:"Enlaces que aparecen al final de la página de historia.",
    fields:[{name:"label", label:"Etiqueta"}, {name:"url", label:"URL"}],
    fromArr:a=>({label:a?.[0]??"", url:a?.[1]??""}), toArr:o=>[o.label||"", o.url||""]},
  sources: {label:"Fuentes generales de la ficha", hint:"Lista de fuentes que aparece al final de la ficha del país.",
    fields:[{name:"label", label:"Etiqueta"}, {name:"url", label:"URL"}],
    fromArr:a=>({label:a?.[0]??"", url:a?.[1]??""}), toArr:o=>[o.label||"", o.url||""]},
  logistics: {label:"Logística (hospitales, fronteras, combustible, agua, consulados...)", hint:"Puntos que aparecen en la capa de emergencias y logística del mapa.",
    fields:[{name:"name", label:"Nombre"}, {name:"cat", label:"Categoría", ph:"Hospital / Frontera / Combustible / Agua potable / Consular"},
      {name:"lat", label:"Latitud", num:true}, {name:"lon", label:"Longitud", num:true}, {name:"info", label:"Información", ta:true}],
    fromArr:o=>({name:o?.name??"", cat:o?.cat??"", lat:o?.lat??"", lon:o?.lon??"", info:o?.info??""}),
    toArr:o=>({name:o.name||"", cat:o.cat||"", lat:parseFloat(o.lat)||0, lon:parseFloat(o.lon)||0, info:o.info||""})},
  custom_sections: {label:"Secciones personalizadas (antes de logística y fuentes)", hint:"Resumen operativo, historia, ruta, agua y combustible… Contenido en HTML.",
    fields:[{name:"id", label:"ID (ancla, sin espacios ni acentos)", ph:"p. ej. resumen"}, {name:"title", label:"Título visible"},
      {name:"html", label:"Contenido (HTML)", ta:true, big:true}],
    fromArr:a=>({id:a?.[0]??"", title:a?.[1]??"", html:a?.[2]??""}), toArr:o=>[o.id||"", o.title||"", o.html||""]},
  custom_sections_post: {label:"Secciones personalizadas (después de logística y fuentes)", hint:"Fronteras, drones, Starlink, perro y salud, seguridad, validación GPX… Contenido en HTML.",
    fields:[{name:"id", label:"ID (ancla, sin espacios ni acentos)"}, {name:"title", label:"Título visible"},
      {name:"html", label:"Contenido (HTML)", ta:true, big:true}],
    fromArr:a=>({id:a?.[0]??"", title:a?.[1]??"", html:a?.[2]??""}), toArr:o=>[o.id||"", o.title||"", o.html||""]},
};

function escHtml(s){ return (s==null?"":String(s)).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
function escAttr(s){ return (s==null?"":String(s)).replace(/&/g,"&amp;").replace(/"/g,"&quot;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

function convertFichaIn(raw){
  const w = {...raw};
  for (const key of Object.keys(REPEATER_DEFS)){
    const def = REPEATER_DEFS[key];
    w[key] = (raw[key] || []).map(def.fromArr);
  }
  return w;
}
function convertFichaOut(w){
  const out = {...w};
  for (const key of Object.keys(REPEATER_DEFS)){
    out[key] = (w[key] || []).map(REPEATER_DEFS[key].toArr);
  }
  return out;
}

function showTab(tab){
  document.getElementById("poiSection").hidden = tab !== "pois";
  document.getElementById("fichaSection").hidden = tab !== "ficha";
  document.getElementById("tabPoisBtn").classList.toggle("active", tab === "pois");
  document.getElementById("tabFichaBtn").classList.toggle("active", tab === "ficha");
}

async function loadFicha(slug){
  try {
    const res = await fetch(`${API}/contents/content/ficha/${slug}.json?ref=${BRANCH}`, {headers: authHeaders()});
    if (res.ok){
      const data = await res.json();
      fichaSha = data.sha;
      fichaWorking = convertFichaIn(JSON.parse(b64ToUtf8(data.content)));
    } else {
      fichaSha = null;
      fichaWorking = convertFichaIn({});
    }
  } catch (e){
    fichaSha = null;
    fichaWorking = convertFichaIn({});
  }
  renderFicha();
}

function renderFicha(){
  const body = document.getElementById("fichaBody");
  if (!body) return;
  let html = '<div class="card"><h2 style="margin-top:0">Datos generales</h2>';
  for (const f of SIMPLE_FIELDS){
    const val = fichaWorking[f.name] ?? "";
    html += `<label>${f.label}</label>`;
    html += f.ta
      ? `<textarea data-simple="${f.name}" style="min-height:90px">${escHtml(val)}</textarea>`
      : `<input type="text" data-simple="${f.name}" value="${escAttr(val)}" placeholder="${escAttr(f.ph||"")}">`;
  }
  html += '</div>';
  for (const key of Object.keys(REPEATER_DEFS)) html += renderRepeaterCard(key);
  html += `<div class="toolbar"><button class="btn" type="button" id="saveFichaBtn">Guardar cambios de la ficha</button></div>`;
  body.innerHTML = html;

  body.querySelectorAll("[data-simple]").forEach(el => {
    el.addEventListener("input", () => { fichaWorking[el.dataset.simple] = el.value; });
  });
  body.querySelectorAll("[data-rep-key]").forEach(el => {
    el.addEventListener("input", () => {
      fichaWorking[el.dataset.repKey][parseInt(el.dataset.repI, 10)][el.dataset.repField] = el.value;
    });
  });
  document.getElementById("saveFichaBtn").addEventListener("click", saveFicha);
}

function renderRepeaterCard(key){
  const def = REPEATER_DEFS[key];
  const items = fichaWorking[key] || [];
  let html = `<div class="card"><h2 style="margin-top:0">${def.label}</h2><p class="hint">${def.hint}</p>`;
  if (!items.length) html += `<p class="hint">Todavía no hay elementos.</p>`;
  items.forEach((item, i) => {
    html += `<div class="rep-item">`;
    def.fields.forEach(f => {
      const val = item[f.name] ?? "";
      html += `<label>${f.label}</label>`;
      html += f.ta
        ? `<textarea data-rep-key="${key}" data-rep-i="${i}" data-rep-field="${f.name}" style="min-height:${f.big?"160px":"70px"}">${escHtml(val)}</textarea>`
        : `<input type="${f.num?"number":"text"}" ${f.num?'step="0.00001"':""} data-rep-key="${key}" data-rep-i="${i}" data-rep-field="${f.name}" value="${escAttr(val)}" placeholder="${escAttr(f.ph||"")}">`;
    });
    html += `<div class="toolbar"><button class="btn danger" type="button" onclick="removeRepItem('${key}',${i})">Borrar este elemento</button></div></div>`;
  });
  html += `<div class="toolbar"><button class="btn ghost" type="button" onclick="addRepItem('${key}')">+ Añadir</button></div></div>`;
  return html;
}

function addRepItem(key){
  const empty = {};
  REPEATER_DEFS[key].fields.forEach(f => empty[f.name] = "");
  (fichaWorking[key] = fichaWorking[key] || []).push(empty);
  renderFicha();
}
function removeRepItem(key, i){
  fichaWorking[key].splice(i, 1);
  renderFicha();
}

async function saveFicha(){
  msg("Guardando ficha en GitHub…", "info");
  try {
    const out = convertFichaOut(fichaWorking);
    const body = {
      message: `Editar ficha: ${currentSlug}`,
      content: utf8ToB64(JSON.stringify(out, null, 2) + "\n"),
      branch: BRANCH,
    };
    if (fichaSha) body.sha = fichaSha;
    const res = await fetch(`${API}/contents/content/ficha/${currentSlug}.json`, {
      method: "PUT", headers: {...authHeaders(), "Content-Type": "application/json"}, body: JSON.stringify(body),
    });
    if (!res.ok){
      const t = await res.text();
      throw new Error("GitHub respondió " + res.status + ": " + t.slice(0, 200));
    }
    const data = await res.json();
    fichaSha = data.content.sha;
    msg("Ficha guardada. El sitio se reconstruye solo en 1-2 minutos.", "ok");
  } catch (e){
    msg("Error al guardar la ficha: " + e.message, "err");
  }
}

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
  fichaSha = null; fichaWorking = {};
  document.getElementById("poiList").innerHTML = "";
  document.getElementById("formCard").hidden = true;
  document.getElementById("fichaBody").innerHTML = "";
  document.getElementById("tabsBar").hidden = !slug;
  if (!slug) return;
  showTab("pois");
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
  loadFicha(slug);
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
  document.getElementById("tabPoisBtn").addEventListener("click", () => showTab("pois"));
  document.getElementById("tabFichaBtn").addEventListener("click", () => showTab("ficha"));
});
"""


def render_admin(countries_for_admin):
    """countries_for_admin: lista de dicts {slug, name} — solo países con content/pois/<slug>.json."""
    countries_json = json.dumps(countries_for_admin, ensure_ascii=False)
    js = (ADMIN_JS.replace("__REPO__", REPO)
                  .replace("__BRANCH__", BRANCH)
                  .replace("__COUNTRIES_JSON__", countries_json))
    body = """<div class="wrap">
<h1>Panel de edición</h1>
<p class="lead">Edita los puntos de interés y el resto de la ficha de cada país (historia, chips, logística, fuentes, secciones...). Los cambios se guardan directamente en GitHub y el sitio se reconstruye y publica solo en 1-2 minutos.</p>

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

  <div class="tabs" id="tabsBar" hidden>
    <button class="tab-btn active" id="tabPoisBtn" type="button">Puntos de interés</button>
    <button class="tab-btn" id="tabFichaBtn" type="button">Ficha del país</button>
  </div>

  <div id="poiSection">
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

  <div id="fichaSection" hidden>
    <div id="fichaBody"></div>
  </div>
</div>
</div>
<script>""" + js + "</script>"
    return body
