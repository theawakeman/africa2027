/* Hoja de cálculo .xlsx del presupuesto, generada en el navegador y sin conexión.
   Todas las casillas de entrada (fondo amarillo) son editables y el resto son
   fórmulas: al cambiar un dato en Excel, Numbers o Google Sheets se recalcula todo. */
(function(){
  // ---------- ZIP mínimo (sin compresión) ----------
  const CRC = (() => { const t = new Uint32Array(256); for (let n = 0; n < 256; n++) { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; t[n] = c >>> 0; } return t; })();
  const crc32 = b => { let c = 0xFFFFFFFF; for (let i = 0; i < b.length; i++) c = CRC[(c ^ b[i]) & 0xFF] ^ (c >>> 8); return (c ^ 0xFFFFFFFF) >>> 0; };
  function zip(files){
    const enc = new TextEncoder(), parts = [], central = []; let off = 0;
    const u16 = v => [v & 255, (v >>> 8) & 255], u32 = v => [v & 255, (v >>> 8) & 255, (v >>> 16) & 255, (v >>> 24) & 255];
    for (const [name, text] of files) {
      const nb = enc.encode(name), data = enc.encode(text), crc = crc32(data);
      const head = [...u32(0x04034b50), ...u16(20), ...u16(0x0800), ...u16(0), ...u16(0), ...u16(0x21),
        ...u32(crc), ...u32(data.length), ...u32(data.length), ...u16(nb.length), ...u16(0)];
      parts.push(new Uint8Array(head), nb, data);
      central.push(new Uint8Array([...u32(0x02014b50), ...u16(20), ...u16(20), ...u16(0x0800), ...u16(0), ...u16(0), ...u16(0x21),
        ...u32(crc), ...u32(data.length), ...u32(data.length), ...u16(nb.length), ...u16(0), ...u16(0), ...u16(0), ...u16(0),
        ...u32(0), ...u32(off)]), nb);
      off += head.length + nb.length + data.length;
    }
    const cdSize = central.reduce((s, p) => s + p.length, 0);
    const end = new Uint8Array([...u32(0x06054b50), ...u16(0), ...u16(0), ...u16(files.length), ...u16(files.length),
      ...u32(cdSize), ...u32(off), ...u16(0)]);
    return new Blob([...parts, ...central, end], {type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'});
  }

  // ---------- Estilos ----------
  // 0 normal · 1 cabecera · 2 € · 3 € negrita · 4 entero · 5 % · 6 decimal · 7 título
  // 8 entrada decimal · 9 entrada € · 10 entrada entero · 11 entrada % · 12 nota · 13 entero negrita · 14 entrada 0/1
  const STYLES = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<numFmts count="4"><numFmt numFmtId="164" formatCode="#,##0.00\\ &quot;€&quot;"/><numFmt numFmtId="165" formatCode="#,##0"/><numFmt numFmtId="166" formatCode="0%"/><numFmt numFmtId="167" formatCode="0.00"/></numFmts>
<fonts count="4"><font><sz val="11"/><name val="Calibri"/></font><font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Calibri"/></font><font><b/><sz val="11"/><name val="Calibri"/></font><font><b/><sz val="15"/><color rgb="FF16324F"/><name val="Calibri"/></font></fonts>
<fills count="4"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FF16324F"/></patternFill></fill><fill><patternFill patternType="solid"><fgColor rgb="FFFCF1DA"/></patternFill></fill></fills>
<borders count="1"><border/></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="15">
<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="top"/></xf>
<xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1" applyAlignment="1"><alignment wrapText="1" vertical="center"/></xf>
<xf numFmtId="164" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>
<xf numFmtId="164" fontId="2" fillId="0" borderId="0" xfId="0" applyNumberFormat="1" applyFont="1"/>
<xf numFmtId="165" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>
<xf numFmtId="166" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>
<xf numFmtId="167" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>
<xf numFmtId="0" fontId="3" fillId="0" borderId="0" xfId="0" applyFont="1"/>
<xf numFmtId="167" fontId="0" fillId="3" borderId="0" xfId="0" applyNumberFormat="1" applyFill="1"/>
<xf numFmtId="164" fontId="0" fillId="3" borderId="0" xfId="0" applyNumberFormat="1" applyFill="1"/>
<xf numFmtId="165" fontId="0" fillId="3" borderId="0" xfId="0" applyNumberFormat="1" applyFill="1"/>
<xf numFmtId="166" fontId="0" fillId="3" borderId="0" xfId="0" applyNumberFormat="1" applyFill="1"/>
<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment wrapText="1" vertical="top"/></xf>
<xf numFmtId="165" fontId="2" fillId="0" borderId="0" xfId="0" applyNumberFormat="1" applyFont="1"/>
<xf numFmtId="0" fontId="0" fillId="3" borderId="0" xfId="0" applyFill="1" applyAlignment="1"><alignment horizontal="center"/></xf>
</cellXfs>
</styleSheet>`;

  const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  const col = n => { let s = ''; n++; while (n) { const m = (n - 1) % 26; s = String.fromCharCode(65 + m) + s; n = Math.floor((n - 1) / 26); } return s; };

  // Hoja: filas de celdas. Celda = texto | número | {f: fórmula, s} | {v, s}
  function sheetXml(rows, widths){
    let x = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">';
    if (widths) x += '<cols>' + widths.map((w, i) => `<col min="${i + 1}" max="${i + 1}" width="${w}" customWidth="1"/>`).join('') + '</cols>';
    x += '<sheetData>';
    rows.forEach((row, r) => {
      if (!row) return;
      x += `<row r="${r + 1}">`;
      row.forEach((c, i) => {
        if (c == null || c === '') return;
        const ref = col(i) + (r + 1);
        const o = (typeof c === 'object') ? c : {v: c};
        const s = o.s != null ? ` s="${o.s}"` : '';
        if (o.f != null) x += `<c r="${ref}"${s}><f>${esc(o.f)}</f></c>`;
        else if (typeof o.v === 'number') x += `<c r="${ref}"${s}><v>${o.v}</v></c>`;
        else x += `<c r="${ref}" t="inlineStr"${s}><is><t xml:space="preserve">${esc(o.v)}</t></is></c>`;
      });
      x += '</row>';
    });
    return x + '</sheetData></worksheet>';
  }

  window.a27PresupuestoXlsx = function(ctx){
    const {D, V, res, PA} = ctx;
    const RU = D.ruta;
    const H = t => ({v: t, s: 1});
    const P = "'Parámetros'!";
    const ref = {};                      // id → referencia absoluta en Parámetros
    const vc = ['B', 'C'];               // columnas de los vehículos en Parámetros
    const EU = {es: 'España', fr: 'Francia', it: 'Italia'};
    const FE = res.FE, fIda = FE[0], fVu = FE[1];
    const eu = r => ({eu: true, n: r.n, tipo: 'de paso', lab: r.nota, km: r.km, dias: null, pr: V(r.gk, r.gd)});
    const filas = [...res.euRows.filter(r => r.key === 'euida').map(eu),
      ...res.ruta.pas.map(p => ({n: PA[p.s].n, tipo: p.tipo === 'visita' ? 'parada' : 'de paso', lab: p.lab || 'enlace aproximado', km: p.km,
        dias: p.dias !== p.diasCalc ? p.dias : null, pr: V('g.' + (p.s === 'cabinda' ? 'angola' : p.s), PA[p.s].gas ? PA[p.s].gas.eur : RU.gas_sin_dato)})),
      ...res.euRows.filter(r => r.key === 'euvuelta').map(eu)];
    const nP = filas.length;
    const g0 = 5, g1 = g0 + nP - 1, gt = g1 + 2;   // filas de la hoja Ruta
    // ---------- Parámetros ----------
    const pr = [];
    pr[0] = [{v: 'África 2027 · Presupuesto por vehículo', s: 7}];
    pr[1] = [{v: 'Casillas con fondo amarillo = datos editables. El resto de hojas se calcula solo a partir de ellas. Ruta: ' + res.ruta.o.map(s => PA[s].n).join(' → '), s: 12}];
    pr[3] = [H('Vehículo'), H(D.vehiculos[0].nombre), H(D.vehiculos[1].nombre), H('Nota')];
    pr[4] = ['Descripción', D.vehiculos[0].detalle, D.vehiculos[1].detalle];
    const vrows = [
      ['l100', 'Consumo medio (L/100 km)', v => V(v.id + '.l100', v.l100), 8, ''],
      ['personas', 'Personas', v => V(v.id + '.personas', v.personas), 10, ''],
      ['perros', 'Perros', v => V(v.id + '.perros', v.perros), 10, ''],
      ['cpd_libro', 'CPD: carnet de 25 hojas (€)', v => V(v.id + '.cpd_libro', v.cpd_libro), 9, 'RACE; importes facilitados el 26-09-2026'],
      ['cpd_banco', 'CPD: costes bancarios del aval (€)', v => V(v.id + '.cpd_banco', v.cpd_banco), 9, 'Sin dato todavía'],
      ['cpd_aval', 'CPD: aval inmovilizado (€, no es gasto)', v => V(v.id + '.cpd_aval', v.cpd_aval), 9, 'Se recupera al cerrar el carnet'],
      ['ferry_ida', `Ferry ida ${fIda.f.origen} → ${fIda.f.puerto} (€)`, v => fIda.precios[D.vehiculos.indexOf(v)], 9, `${fIda.f.naviera} · ${fIda.f.nota}`],
      ['ferry_vuelta', `Ferry vuelta ${fVu.f.puerto} → ${fVu.f.origen} (€)`, v => fVu.precios[D.vehiculos.indexOf(v)], 9, `${fVu.f.naviera} · ${fVu.f.nota}`],
    ];
    vrows.forEach(([id, label, fn, st, nota], k) => {
      const r = 5 + k;
      pr[r] = [label, {v: fn(D.vehiculos[0]), s: st}, {v: fn(D.vehiculos[1]), s: st}, {v: nota, s: 12}];
      ref[id] = i => `${P}$${vc[i]}$${r + 1}`;
    });
    let r = 5 + vrows.length + 1;
    pr[r] = [H('Parámetro del viaje'), H('Valor'), H('Unidad'), H('Tipo / nota')];
    const gen = [
      ['ritmo_v', 'Ritmo en países de parada', res.rv, 10, 'km/día', 'Estimación, contando los días de parada'],
      ['ritmo_t', 'Ritmo en países de paso', res.rt, 10, 'km/día', 'Estimación'],
      ['margen', 'Margen de días', res.margen, 11, '%', 'Fronteras, trámites, averías, lluvia'],
      ['dias_ferry', 'Días de ferry (ida + vuelta)', fIda.diasFerry + fVu.diasFerry, 8, 'días', `${fIda.f.h} h + ${fVu.f.h} h de travesía`],
      ['dias_fijos', 'Duración fija (0 = calcular)', res.fijos, 10, 'días', 'Si vale más de 0, sustituye a la duración calculada'],
      ['dias', 'Días de viaje', null, 13, 'días', 'Fórmula: días de la hoja Ruta × (1 + margen) + ferry, o la duración fija'],
      ['factor', 'Factor de ajuste de km', res.factor, 8, '×', 'Los km ya son por carretera (OSRM); 1 = sin ajuste'],
      ['desvios', 'Desvíos fuera del corredor', res.desv, 11, '%', 'Agua, gasoil, trámites'],
      ['perro_ferry', 'Perro en el ferry', D.perro_ferry, 9, '€ / trayecto', 'Estimación: GNV no publica el precio'],
    ];
    D.params.forEach(p => {
      const pct = p.ambito === 'pct';
      gen.push([p.id, p.label, pct ? V('p.' + p.id, p.val) / 100 : V('p.' + p.id, p.val), pct ? 11 : 9, pct ? '% del total' : p.unidad,
        (p.tipo === 'dato' ? 'Dato' : 'Estimación') + (p.nota ? ' · ' + p.nota : '')]);
    });
    gen.forEach(([id, label, val, st, unidad, nota]) => {
      r++;
      ref[id] = `${P}$B$${r + 1}`;
      const cell = id === 'dias'
        ? {f: `IF(${ref.dias_fijos}>0,${ref.dias_fijos},ROUNDUP((Ruta!J${gt}+${ref.dias_ferry})*(1+${ref.margen}),0))`, s: st}
        : {v: val, s: st};
      pr[r] = [label, cell, unidad, {v: nota, s: 12}];
    });
    const personasTot = `(${ref.personas(0)}+${ref.personas(1)})`;
    // ---------- Ruta y combustible ----------
    const cr = [];
    cr[0] = [{v: 'Ruta, días y combustible', s: 7}];
    cr[1] = [{v: 'Salida y regreso por ' + RU.origen + '. Una fila por cada entrada en un país, en orden de marcha, más la carretera en Europa hasta el puerto. Km base: OSRM por el corredor de la ficha en las paradas; línea recta × 1,25 en enlaces y países de paso. Km estimados = km base × factor × (1 + desvíos). Días = km ÷ ritmo, salvo que se escriba una cifra en «Días fijados».', s: 12}];
    cr[3] = ['#', 'País', 'Tipo', 'Recorrido', 'Km base', 'Km estimados', 'Ritmo km/día', 'Días calculados', 'Días fijados', 'Días', '€/litro',
      'Litros ' + D.vehiculos[0].nombre, '€ ' + D.vehiculos[0].nombre, 'Litros ' + D.vehiculos[1].nombre, '€ ' + D.vehiculos[1].nombre].map(H);
    filas.forEach((p, k) => {
      const n = g0 + k, pr1 = p.pr;
      const ov = p.dias != null ? {v: p.dias, s: 8} : {v: '', s: 8};
      cr[n - 1] = [k + 1, p.n, p.tipo, {v: p.lab, s: 12}, {v: Math.round(p.km), s: 10},
        {f: p.eu ? `E${n}` : `E${n}*${ref.factor}*(1+${ref.desvios})`, s: 4},
        {f: `IF(C${n}="parada",${ref.ritmo_v},${ref.ritmo_t})`, s: 4},
        {f: `F${n}/G${n}`, s: 6}, ov.v === '' ? {v: ' ', s: 8} : ov, {f: `IF(ISNUMBER(I${n}),I${n},H${n})`, s: 6},
        {v: pr1, s: 9},
        {f: `F${n}*${ref.l100(0)}/100`, s: 4}, {f: `L${n}*K${n}`, s: 2},
        {f: `F${n}*${ref.l100(1)}/100`, s: 4}, {f: `N${n}*K${n}`, s: 2}];
    });
    cr[gt - 1] = [null, {v: 'TOTAL', s: 1}, null, null, {f: `SUM(E${g0}:E${g1})`, s: 13}, {f: `SUM(F${g0}:F${g1})`, s: 13}, null, null, null,
      {f: `SUM(J${g0}:J${g1})`, s: 6}, null, {f: `SUM(L${g0}:L${g1})`, s: 13}, {f: `SUM(M${g0}:M${g1})`, s: 3}, {f: `SUM(N${g0}:N${g1})`, s: 13}, {f: `SUM(O${g0}:O${g1})`, s: 3}];
    // ---------- Visados ----------
    const vr = [];
    vr[0] = [{v: 'Visados (el importe es por persona)', s: 7}];
    vr[1] = [{v: '«Visados por persona» = cuántos visados necesita CADA viajero en ese país: uno por entrada con la ruta elegida (1 si se saca uno de entradas múltiples). La última columna multiplica por todas las personas de Parámetros.', s: 12}];
    vr[3] = ['País', '€ por visado', 'Visados por persona', 'Por persona', 'Todas las personas', 'Nota', 'Fuente'].map(H);
    const v0 = 5, VO = res.visOut;
    VO.forEach((v, k) => {
      const n = v0 + k;
      vr[n - 1] = [PA[v.s].n, {v: v.eur, s: 9}, {v: v.n, s: 10}, {f: `B${n}*C${n}`, s: 2}, {f: `D${n}*${personasTot}`, s: 2}, {v: v.txt, s: 12}, v.url];
    });
    const v1 = v0 + Math.max(VO.length, 1) - 1, vt = v1 + 2;
    vr[vt - 1] = [{v: 'TOTAL', s: 1}, null, null, {f: `SUM(D${v0}:D${v1})`, s: 3}, {f: `SUM(E${v0}:E${v1})`, s: 3}];
    const sinV = res.orden.filter(s => PA[s].vis === 'sin' && !PA[s].solo_paso).map(s => PA[s].n);
    vr[vt + 1] = [{v: 'Sin visado: ' + (sinV.join(', ') || '—'), s: 12}];
    // ---------- Tasas de frontera ----------
    const tr = [];
    tr[0] = [{v: 'Tasas de importación temporal en frontera (por vehículo)', s: 7}];
    tr[1] = [{v: 'Importe por entrada × entradas de la ruta elegida. Donde no hay dato publicado el importe es 0: rellenarlo cuando se conozca.', s: 12}];
    tr[3] = ['País', '€ por entrada', 'Entradas', '€ por vehículo', 'Nota'].map(H);
    const t0 = 5, TO = res.tasOut;
    TO.forEach((v, k) => {
      const n = t0 + k;
      tr[n - 1] = [PA[v.s].n, {v: v.eur, s: 9}, {v: v.n, s: 10}, {f: `B${n}*C${n}`, s: 2}, {v: v.txt, s: 12}];
    });
    const t1 = t0 + Math.max(TO.length, 1) - 1, tt = t1 + 2;
    tr[tt - 1] = [{v: 'TOTAL', s: 1}, null, null, {f: `SUM(D${t0}:D${t1})`, s: 3}];
    // ---------- Resumen ----------
    const R = [];
    R[0] = [{v: 'Resumen del presupuesto', s: 7}];
    R[1] = [{v: 'Todo son fórmulas: se actualiza al cambiar Parámetros, Ruta, Visados o Tasas.', s: 12}];
    R[3] = [H('Partida'), H(D.vehiculos[0].nombre + ' · ' + D.vehiculos[0].detalle), H(D.vehiculos[1].nombre + ' · ' + D.vehiculos[1].detalle), H('Total')];
    const p = id => ref[id];
    const lines = [
      ['Combustible', i => `Ruta!${i ? 'O' : 'M'}${gt}`],
      ['Visados', i => `Visados!D${vt}*${ref.personas(i)}`],
      ['Vehículo: CPD, tasas, seguros, mantenimiento', i => `${ref.cpd_libro(i)}+${ref.cpd_banco(i)}+'Tasas frontera'!D${tt}+${p('seguros')}+${p('mantenimiento')}`],
      ['Ferris (ida y vuelta)', i => `${ref.ferry_ida(i)}+${ref.ferry_vuelta(i)}`],
      ['Comida, noches y actividades', i => `${p('comida')}*${ref.personas(i)}*${p('dias')}+${p('noche')}*${p('dias')}+${p('parques')}*${ref.personas(i)}`],
      ['Perro (comida, trámites y ferry)', i => `${ref.perros(i)}*(${p('perro_comida')}*${p('dias')}+${p('perro_tramites')}+2*${p('perro_ferry')})`],
      ['Comunicaciones', i => `${p('comunicaciones')}*${p('dias')}/30.4`],
    ];
    const r0 = 5;
    lines.forEach(([label, fn], k) => {
      const n = r0 + k;
      R[n - 1] = [label, {f: fn(0), s: 2}, {f: fn(1), s: 2}, {f: `B${n}+C${n}`, s: 3}];
    });
    const rl = r0 + lines.length - 1, rs = rl + 1, ri = rl + 2, rt = rl + 3;
    R[rs - 1] = [{v: 'Subtotal', s: 1}, {f: `SUM(B${r0}:B${rl})`, s: 3}, {f: `SUM(C${r0}:C${rl})`, s: 3}, {f: `B${rs}+C${rs}`, s: 3}];
    R[ri - 1] = ['Imprevistos', {f: `B${rs}*${p('imprevistos')}`, s: 2}, {f: `C${rs}*${p('imprevistos')}`, s: 2}, {f: `B${ri}+C${ri}`, s: 3}];
    R[rt - 1] = [{v: 'TOTAL', s: 1}, {f: `B${rs}+B${ri}`, s: 3}, {f: `C${rs}+C${ri}`, s: 3}, {f: `B${rt}+C${rt}`, s: 3}];
    R[rt + 1] = ['Por persona', {f: `IF(${ref.personas(0)}>0,B${rt}/${ref.personas(0)},0)`, s: 2}, {f: `IF(${ref.personas(1)}>0,C${rt}/${ref.personas(1)},0)`, s: 2}, {f: `D${rt}/${personasTot}`, s: 2}];
    R[rt + 2] = ['Por día', {f: `B${rt}/${p('dias')}`, s: 2}, {f: `C${rt}/${p('dias')}`, s: 2}, {f: `D${rt}/${p('dias')}`, s: 2}];
    R[rt + 3] = ['Kilómetros por vehículo', {f: `Ruta!F${gt}`, s: 4}];
    R[rt + 4] = ['Litros de gasóleo', {f: `Ruta!L${gt}`, s: 4}, {f: `Ruta!N${gt}`, s: 4}, {f: `B${rt + 5}+C${rt + 5}`, s: 13}];
    R[rt + 5] = ['Aval CPD inmovilizado (no suma al total; se recupera)', {f: ref.cpd_aval(0), s: 2}, {f: ref.cpd_aval(1), s: 2}, {f: `B${rt + 6}+C${rt + 6}`, s: 2}];
    R[rt + 6] = ['Dinero comprometido al salir (total + avales)', {f: `B${rt}+B${rt + 6}`, s: 3}, {f: `C${rt}+C${rt + 6}`, s: 3}, {f: `D${rt}+D${rt + 6}`, s: 3}];
    R[rt + 7] = ['Días de viaje', {f: p('dias'), s: 13}, {v: 'Salida ' + res.salida + ' · regreso con los valores de la web: ' + res.regreso, s: 12}];
    const sheets = [
      ['Resumen', sheetXml(R, [46, 30, 30, 16])],
      ['Parámetros', sheetXml(pr, [44, 18, 18, 70])],
      ['Ruta', sheetXml(cr, [5, 22, 10, 50, 10, 11, 10, 10, 10, 8, 9, 12, 12, 12, 12])],
      ['Visados', sheetXml(vr, [24, 13, 13, 12, 14, 70, 50])],
      ['Tasas frontera', sheetXml(tr, [24, 13, 10, 14, 80])],
    ];
    const files = [
      ['[Content_Types].xml', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
        + sheets.map((_, i) => `<Override PartName="/xl/worksheets/sheet${i + 1}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>`).join('') + '</Types>'],
      ['_rels/.rels', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>'],
      ['xl/workbook.xml', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>'
        + sheets.map(([n], i) => `<sheet name="${esc(n)}" sheetId="${i + 1}" r:id="rId${i + 1}"/>`).join('') + '</sheets><calcPr calcId="191029" fullCalcOnLoad="1"/></workbook>'],
      ['xl/_rels/workbook.xml.rels', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        + sheets.map((_, i) => `<Relationship Id="rId${i + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet${i + 1}.xml"/>`).join('')
        + `<Relationship Id="rId${sheets.length + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>`],
      ['xl/styles.xml', STYLES],
      ...sheets.map(([, xml], i) => [`xl/worksheets/sheet${i + 1}.xml`, xml]),
    ];
    return zip(files);
  };
})();
