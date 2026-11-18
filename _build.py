# -*- coding: utf-8 -*-
"""Чек-лист 4 дня — для СПК-наставника. Захаров Альберт, 17–20.11.2026. Не трогает основной чек-лист."""
from pathlib import Path
import html

OUT = Path(__file__).resolve().parent / "index.html"
ASSETS = Path(__file__).resolve().parent.parent / "assets"


def esc(s):
    return html.escape(s, quote=True)


def item(text):
    return f"""
    <label class="item">
      <input type="checkbox" data-k />
      <span class="box" aria-hidden="true"></span>
      <span class="txt">{esc(text)}</span>
    </label>"""


def items(texts):
    return "\n".join(item(t) for t in texts)


def section(title, body, note=""):
    note_html = f'<p class="when">{esc(note)}</p>' if note else ""
    return f"""
    <section class="block">
      <h2>{esc(title)}</h2>
      {note_html}
      <div class="list">{body}</div>
    </section>"""


def field(label, value=""):
    val = f' value="{esc(value)}"' if value else ""
    return f"""
    <label class="field">
      <span>{esc(label)}</span>
      <input type="text" data-k class="ink" autocomplete="off"{val} />
    </label>"""


# 4 дня = сжатые 3 недели + день закрепления. Заполняет наставник-СПК.
day1 = [
    "08:00–08:30. Пятиминутка со СПК: задачи дня, внешний вид смены",
    "08:30–09:30. Обход точки: улица, касса, зал, склад. Ценники, чистота, товар в зале",
    "09:30–11:00. Битрикс24 и отчёты 1С: задачи, план/факт, ТО, неликвиды",
    "11:00–12:30. Управление командой: постановка задач, контроль, мин-макс / крючки / «извиняшки»",
    "12:30–13:00. Обед",
    "13:00–14:30. ПК: продажа — встреча, потребность, оффер, закрытие, сопутка",
    "14:30–15:30. МОП: карточка юрлица, условия, как СПК контролирует отгрузку и документы",
    "15:30–16:30. Практика: обход + задачи смене + 1–2 продажи в зале",
    "16:30–17:00. Итог дня со СПК: что закрыто, что доучить. Вечерняя закатка / контроль зала",
    "Проверка дня 1 (СПК): день рядом с СПК закрыт без критичных срывов",
]

day2 = [
    "08:00–08:30. Склад: зоны, брак, ворота, маршрут приёмки",
    "08:30–10:00. 1С:Торговля + ТСД: остаток, карточка, документы склада",
    "10:00–12:00. Приёмка: с РЦ и/или от поставщика (живая или учебный разбор)",
    "12:00–12:30. Перемещения, подготовка к РЦ / ИМ; брак и минусы",
    "12:30–13:00. Обед",
    "13:00–14:30. Сборка автозаказа / заказа ИМ; выдача",
    "14:30–15:30. ПК: сборка техники с РТЗ (одна позиция). МОП: подготовка к корпоративной отгрузке",
    "15:30–16:30. Практика: закрытие дня склада — 1С, ТСД, ворота",
    "16:30–17:00. Итог дня с кладовщиком: что закрыто, что доучить",
    "Проверка дня 2 (кладовщик): ключевые операции склада сделаны под контролем / сам",
]

day3 = [
    "08:00–08:30. Открытие смены на кассе: расходники, терминал",
    "08:30–10:30. Касса: продажа нал/карта, сдача, возврат, размен",
    "10:30–12:00. КСО, весовой товар, сертификаты, скидки, акции, ценники",
    "12:00–12:30. Допродажи на кассе: сопутка",
    "12:30–13:00. Обед",
    "13:00–14:30. ПК: продажи в зале + аналитика своих чеков. МОП: доверенность, УПД, ЭДО, оплата юрлица",
    "14:30–16:00. Практика: самостоятельная работа на кассе под контролем",
    "16:00–16:40. Вечерний кассовый отчёт; действия при ошибке терминала",
    "16:40–17:00. Итог дня с кассиром: что закрыто, что доучить",
    "Проверка дня 3 (кассир): день на кассе закрыт",
]

day4 = [
    "08:00–08:30. Пятиминутка: план дня 4 — слабые места и готовность к Успенке",
    "08:30–10:30. Закрепление СПК: обход, задачи смене, Битрикс24, мин-макс / крючки под контролем наставника",
    "10:30–12:00. Закрепление по складу или кассе — то, что в дни 2–3 осталось слабым",
    "12:00–12:30. ПК / РТЗ: выкладка, ценники, улица; при необходимости сборка техники",
    "12:30–13:00. Обед",
    "13:00–14:30. МОП / заказы: один полный цикл или учебный разбор до конца",
    "14:30–16:00. Практика: стажёр ведёт смену рядом с наставником без подсказок на каждом шаге",
    "16:00–16:40. Проверка по ролям: СПК, кладовщик, кассир, ПК, МОП — что закрыто",
    "16:40–17:00. Итог 4 дней: допуск к работе в Успенке / список доучить",
    "Проверка дня 4: готовность выходить СПК Успенка — да / доучить",
]

checks = [
    "СПК: основные навыки дня 1 и закрепление дня 4 закрыты",
    "Кладовщик: основные навыки дня 2 закрыты",
    "Кассир: основные навыки дня 3 закрыты",
    "ПК: продажа / допродажа / выкладка или сборка — отработано в дни 1–4",
    "МОП: юрлицо / документы / ЭДО или отгрузка — отработано в дни 1–4",
    "Критичных дыр нет — можно выходить СПК в магазин Успенка / доучить по списку",
]

sections_html = "".join([
    section(
        "День 1 · 17.11.2026 · СПК",
        items(day1),
        "08:00–17:00 · Перевалово · с наставником Суковатой Ольгой · внутри дня — ПК и МОП",
    ),
    section(
        "День 2 · 18.11.2026 · Кладовщик",
        items(day2),
        "08:00–17:00 · Перевалово · с кладовщиком · внутри дня — сборка (ПК) и отгрузка (МОП)",
    ),
    section(
        "День 3 · 19.11.2026 · Кассир",
        items(day3),
        "08:00–17:00 · Перевалово · с кассиром · внутри дня — продажи/чеки (ПК) и документы/ЭДО (МОП)",
    ),
    section(
        "День 4 · 20.11.2026 · Закрепление и допуск",
        items(day4),
        "08:00–17:00 · Перевалово · со СПК-наставником · слабые места + готовность к Успенке",
    ),
    section(
        "Проверка по ролям (обязательно)",
        items(checks),
        "За 4 дня — минимум по каждой роли. Что не закрыто — в комментарий.",
    ),
])

doc = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Чек-лист 4 дня — Захаров Альберт — Академия УМ</title>
  <meta name="description" content="Экспресс-стажировка СПК: 4 дня 17–20.11.2026. Захаров Альберт, Успенка. Наставник Суковатая Ольга, Перевалово. Для СПК-наставника." />
  <meta name="theme-color" content="#222222" />
  <style>
    :root {{
      --ink: #222222;
      --paper: #ffffff;
      --page-w: 210mm;
      --font: Arial, "Helvetica Neue", Helvetica, sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      font-family: var(--font);
      font-size: 15px;
      line-height: 1.45;
      background: #f0f0f0;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}
    .toolbar {{
      position: sticky; top: 0; z-index: 50;
      display: flex; flex-wrap: wrap; gap: 8px; align-items: center;
      justify-content: space-between;
      padding: 8px 12px;
      background: #555;
      color: #fff;
      font-size: 12px;
    }}
    .toolbar .brand {{ display: flex; align-items: center; gap: 8px; }}
    .toolbar .brand img {{
      height: 28px; width: auto;
      background: #fff; padding: 2px 4px;
      filter: grayscale(1) opacity(0.85);
    }}
    .toolbar .actions {{ display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }}
    .toolbar button {{
      border: 1px solid #ccc;
      background: transparent;
      color: #fff;
      font: inherit;
      font-size: 12px;
      padding: 5px 10px;
      cursor: pointer;
    }}
    .toolbar button.primary {{ background: #fff; color: #444; border-color: #fff; }}
    .toolbar .status {{ font-size: 11px; opacity: .85; }}
    .sheet-wrap {{
      width: min(var(--page-w), calc(100% - 16px));
      margin: 12px auto 32px;
    }}
    .sheet {{
      background: var(--paper);
      border: 1px solid #bbb;
      box-shadow: 0 1px 6px rgba(0,0,0,.08);
      padding: 16px 18px 22px;
    }}
    .motto {{
      text-align: center;
      color: #888;
      font-size: 12px;
      margin: 0 0 8px;
      letter-spacing: .04em;
    }}
    .title-block {{
      text-align: center;
      margin: 0 0 14px;
      padding: 0 0 10px;
      border-bottom: 1px solid #ccc;
    }}
    .title-block .logo {{
      display: block;
      width: min(140px, 42%);
      height: auto;
      margin: 0 auto 6px;
      filter: grayscale(1) opacity(0.75);
    }}
    .eyebrow {{ margin: 0; font-size: 11px; color: #999; }}
    h1 {{
      font-weight: 600;
      font-size: 18px;
      line-height: 1.25;
      margin: 4px 0 2px;
      color: #555;
    }}
    .meta {{ display: grid; gap: 8px; margin: 0 0 12px; }}
    .field {{
      display: grid;
      grid-template-columns: 200px 1fr;
      gap: 8px;
      align-items: end;
      font-size: 14px;
    }}
    .field span {{ color: #444; padding-bottom: 2px; }}
    .field .ink, .admit .ink {{
      border: none;
      border-bottom: 1px solid #999;
      background: transparent;
      font: inherit;
      font-size: 15px;
      padding: 2px 4px;
      width: 100%;
    }}
    .scheme {{
      margin: 0 0 16px;
      font-size: 13px;
      color: #555;
      line-height: 1.45;
    }}
    .scheme b {{ font-weight: 600; color: #444; }}
    .block {{ margin: 0 0 16px; page-break-inside: avoid; }}
    h2 {{
      font-weight: 600;
      font-size: 16px;
      color: #444;
      margin: 0 0 6px;
    }}
    .when {{ margin: 0 0 8px; font-size: 13px; color: #777; }}
    .list {{ display: flex; flex-direction: column; gap: 6px; }}
    .item {{
      display: grid;
      grid-template-columns: 18px 1fr;
      gap: 8px;
      align-items: start;
      cursor: pointer;
      font-size: 15px;
      line-height: 1.4;
    }}
    .item input {{
      position: absolute;
      opacity: 0;
      width: 1px;
      height: 1px;
      pointer-events: none;
    }}
    .item .box {{
      width: 16px;
      height: 16px;
      margin-top: 2px;
      border: 1.5px solid #666;
      background: #fff;
    }}
    .item input:checked + .box {{
      background: #555;
      border-color: #555;
      box-shadow: inset 0 0 0 2px #fff;
    }}
    .admit {{
      margin: 18px 0 12px;
      padding-top: 12px;
      border-top: 1px solid #ccc;
    }}
    .admit-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px 18px;
      align-items: center;
      margin: 0 0 10px;
      font-size: 15px;
    }}
    .admit-row .choice {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }}
    .admit-row .choice input {{ width: 16px; height: 16px; }}
    .sign {{ display: grid; gap: 8px; margin-top: 8px; }}
    .sign .field {{ grid-template-columns: 180px 1fr; }}
    @media (max-width: 640px) {{
      .field, .sign .field {{ grid-template-columns: 1fr; gap: 2px; }}
    }}
    @media print {{
      .toolbar {{ display: none !important; }}
      body {{ background: #fff; font-size: 14px; }}
      .sheet-wrap {{ width: 100%; margin: 0; }}
      .sheet {{ border: none; box-shadow: none; padding: 0; }}
      .title-block .logo {{ width: 110px; filter: grayscale(1) opacity(0.55); }}
      .item {{ font-size: 13px; }}
      .item .box {{ width: 13px; height: 13px; border-width: 1px; }}
      .block {{ break-inside: avoid; }}
    }}
  </style>
</head>
<body>
  <div class="toolbar" role="banner">
    <div class="brand">
      <img src="assets/logo.png" alt="У Михалыча" width="120" height="36" />
      <span>Академия УМ · Захаров · 4 дня · для СПК</span>
    </div>
    <div class="actions">
      <span class="status" id="save-status">онлайн-сохранение в этом браузере</span>
      <button type="button" id="btn-save">Сохранить</button>
      <button type="button" id="btn-clear">Очистить</button>
      <button type="button" class="primary" id="btn-print">Печать / PDF</button>
    </div>
  </div>

  <div class="sheet-wrap">
    <article class="sheet" id="checklist">
      <p class="motto">Делаем мир крепче</p>
      <header class="title-block">
        <img class="logo" src="assets/logo.png" alt="У Михалыча" width="250" height="72" />
        <p class="eyebrow">Академия УМ · сеть «У Михалыча»</p>
        <h1>Чек-лист 4 дня · для СПК-наставника</h1>
      </header>

      <div class="meta">
        {field("Стажёр", "Захаров Альберт")}
        {field("Должность", "СПК Успенка")}
        {field("Место стажировки", "Перевалово")}
        {field("Даты", "17.11.2026 · 18.11.2026 · 19.11.2026 · 20.11.2026")}
        {field("График", "08:00–17:00")}
        {field("Наставник", "Суковатая Ольга, СПК Перевалово")}
      </div>

      <p class="scheme">
        <b>Заполняет наставник-СПК</b> Суковатая Ольга.<br />
        <b>Захаров Альберт</b> — новый СПК Успенка, стажируется в Перевалово с 17 по 20 ноября 2026.<br />
        <b>Экспресс 4 дня:</b> день 1 — СПК · день 2 — кладовщик · день 3 — кассир · день 4 — закрепление и допуск.
        ПК и МОП — внутри дней. Только основные навыки.
      </p>

      {sections_html}

      <section class="admit">
        <h2>Итог 20.11.2026</h2>
        <div class="admit-row">
          <span>Готов к работе СПК Успенка:</span>
          <label class="choice"><input type="checkbox" data-k /> Да</label>
          <label class="choice"><input type="checkbox" data-k /> Нет / доучить</label>
        </div>
        {field("Что доучить")}
        <div class="sign">
          {field("Подпись наставника", "Суковатая Ольга")}
          {field("Подпись стажёра", "Захаров Альберт")}
          {field("Дата", "20.11.2026")}
        </div>
      </section>
    </article>
  </div>

  <script>
  (function () {{
    const KEY = "um-academy-spk-zaharov-4days-20261117";
    const root = document.getElementById("checklist");
    const status = document.getElementById("save-status");
    const fields = () => root.querySelectorAll("[data-k]");

    function assignIds() {{
      fields().forEach((el, i) => {{
        if (!el.dataset.id) el.dataset.id = "f" + i;
      }});
    }}

    function collect() {{
      const data = {{}};
      fields().forEach((el) => {{
        const id = el.dataset.id;
        if (el.type === "checkbox") data[id] = el.checked;
        else data[id] = el.value;
      }});
      return data;
    }}

    function apply(data) {{
      if (!data) return;
      fields().forEach((el) => {{
        const id = el.dataset.id;
        if (!(id in data)) return;
        if (el.type === "checkbox") el.checked = !!data[id];
        else if (!el.value) el.value = data[id] || "";
        else if (data[id]) el.value = data[id];
      }});
    }}

    function save(manual) {{
      try {{
        localStorage.setItem(KEY, JSON.stringify(collect()));
        const t = new Date();
        status.textContent = (manual ? "сохранено " : "автосохранение ") +
          t.toLocaleTimeString("ru-RU", {{ hour: "2-digit", minute: "2-digit" }});
      }} catch (e) {{
        status.textContent = "не удалось сохранить";
      }}
    }}

    function load() {{
      try {{
        const raw = localStorage.getItem(KEY);
        if (raw) apply(JSON.parse(raw));
      }} catch (e) {{}}
    }}

    assignIds();
    load();

    let timer;
    root.addEventListener("input", () => {{
      clearTimeout(timer);
      timer = setTimeout(() => save(false), 400);
    }});
    root.addEventListener("change", () => save(false));
    document.getElementById("btn-save").addEventListener("click", () => save(true));
    document.getElementById("btn-print").addEventListener("click", () => {{
      save(true);
      window.print();
    }});
    document.getElementById("btn-clear").addEventListener("click", () => {{
      if (!confirm("Очистить отметки в этом браузере?")) return;
      fields().forEach((el) => {{
        if (el.type === "checkbox") el.checked = false;
        else if (!el.defaultValue) el.value = "";
        else el.value = el.defaultValue;
      }});
      localStorage.removeItem(KEY);
      status.textContent = "очищено";
    }});
  }})();
  </script>
</body>
</html>
"""

OUT.write_text(doc, encoding="utf-8")
# copy logo if needed
import shutil
assets_out = Path(__file__).resolve().parent / "assets"
assets_out.mkdir(exist_ok=True)
logo = ASSETS / "logo.png"
if logo.exists():
    shutil.copy2(logo, assets_out / "logo.png")
print("OK", OUT, "bytes", OUT.stat().st_size)
