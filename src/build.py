#!/usr/bin/env python3
"""Static generator for foodporter.nl. NL at /, EN at /en/. Run: python3 src/build.py"""
import os, html, datetime
ROOT = os.path.join(os.path.dirname(__file__), "..", "site")
BASE = "https://foodporter.nl"
APP = "https://app.foodporter.nl"
# slug per page: (nl path, en path)
PAGES = {
 "home": ("/", "/en/"), "customers": ("/klanten/", "/en/customers/"),
 "restaurants": ("/restaurants/", "/en/restaurants/"), "riders": ("/bezorgers/", "/en/riders/"),
 "about": ("/over-ons/", "/en/about/"), "faq": ("/veelgestelde-vragen/", "/en/faq/"),
 "contact": ("/contact/", "/en/contact/"), "legal": ("/juridisch/", "/en/legal/"),
}
NAV = ["customers", "restaurants", "riders", "about", "faq", "contact"]
T = {
 "customers": ("Klanten", "Customers"), "restaurants": ("Restaurants", "Restaurants"),
 "riders": ("Bezorgers", "Riders"), "about": ("Over ons", "About"), "faq": ("FAQ", "FAQ"),
 "contact": ("Contact", "Contact"), "legal": ("Juridisch", "Legal"), "home": ("Home", "Home"),
}
PLACE = '<mark class="ph">[{}]</mark>'
def ph(nl, en, L): return PLACE.format(nl if L == 0 else en)

FEES = lambda L: f"""<table class="fees"><caption>{("Bezorgkosten","Delivery fees")[L]}</caption>
<thead><tr><th scope="col">{("Afstand","Distance")[L]}</th><th scope="col">{("Prijs","Price")[L]}</th></tr></thead><tbody>
<tr><td>{("tot 3 km","up to 3 km")[L]}</td><td>€ 2,49</td></tr>
<tr><td>3–5 km</td><td>€ 3,49</td></tr>
<tr><td>5–10 km</td><td>€ 4,99</td></tr>
<tr><td>{("Servicekosten per bestelling","Service fee per order")[L]}</td><td>€ 0,99</td></tr></tbody></table>
<p class="small">{("Bij de start bezorgen we binnen ongeveer 5 km van het centrum van Tilburg. De app toont altijd de exacte prijs voordat je betaalt.","At launch we deliver within about 5 km of Tilburg city centre. The app always shows the exact price before you pay.")[L]}</p>"""
if True:
    pass

def btn(href, label, cls="btn"): return f'<a class="{cls}" href="{href}">{label}</a>'
ORDER = lambda L: btn(APP + "/", ("Bestel in de app", "Order in the app")[L])

def body(page, L):
    n = lambda a, b: (a, b)[L]
    if page == "home":
        return f"""<section class="hero"><div class="wrap hero-in"><div>
<p class="eyebrow">{n("Tilburg · start 1 januari 2027","Tilburg · launching 1 January 2027")}</p>
<h1>{n("Lokaal eten, eerlijk bezorgd.","Local food, delivered fairly.")}</h1>
<p class="lead">{n("Food Porter brengt gerechten van restaurants uit Tilburg naar je deur, met bezorgers die bij ons in dienst zijn.","Food Porter brings dishes from Tilburg restaurants to your door, with riders we employ directly.")}</p>
<p class="ctas">{ORDER(L)} {btn(PAGES['restaurants'][L], n("Voor restaurants","For restaurants"), "btn btn-alt")}</p>
<p class="small">{n("We zitten in de testfase: je kunt rondkijken, maar er worden nog geen echte betalingen verwerkt.","We are in a test phase: you can look around, but no real payments are processed yet.")}</p></div>
<img src="/assets/logo-full.png" width="403" height="225" alt="Food Porter logo: rider on a scooter between two location pins"></div></section>
<section class="wrap"><h2>{n("Zo werkt het","How it works")}</h2><ol class="steps">
<li><h3>{n("Kies","Choose")}</h3><p>{n("Open de app en kies een restaurant in Tilburg.","Open the app and pick a restaurant in Tilburg.")}</p></li>
<li><h3>{n("Bestel","Order")}</h3><p>{n("Stel je bestelling samen en betaal veilig met iDEAL of kaart.","Build your order and pay securely with iDEAL or card.")}</p></li>
<li><h3>{n("Volg","Track")}</h3><p>{n("Volg je bestelling live tot de bezorger aanbelt, of haal hem zelf op.","Follow your order live until the rider rings, or pick it up yourself.")}</p></li></ol></section>
<section class="band"><div class="wrap grid3">
<div class="card"><h3>{n("Voor klanten","For customers")}</h3><p>{n("Duidelijke prijzen vooraf, allergenenfilter en live volgen.","Clear prices upfront, allergen filter and live tracking.")}</p><a href="{PAGES['customers'][L]}">{n("Meer voor klanten","More for customers")} →</a></div>
<div class="card"><h3>{n("Voor restaurants","For restaurants")}</h3><p>{n("Lage commissie, eigen tablet-overzicht en wekelijkse uitbetaling.","Low commission, your own order screen and regular payouts.")}</p><a href="{PAGES['restaurants'][L]}">{n("Partner worden","Become a partner")} →</a></div>
<div class="card"><h3>{n("Voor bezorgers","For riders")}</h3><p>{n("Gewoon in dienst, met cao, pensioen en 100% van je fooien.","Properly employed, with collective agreement, pension and 100% of your tips.")}</p><a href="{PAGES['riders'][L]}">{n("Werken als bezorger","Work as a rider")} →</a></div></div></section>"""
    if page == "customers":
        return f"""<section class="wrap narrow"><h1>{n("Bestellen bij Food Porter","Ordering with Food Porter")}</h1>
<p class="lead">{n("Eten van lokale restaurants, zonder verrassingen bij het afrekenen.","Food from local restaurants, with no surprises at checkout.")}</p>
<ul class="checks"><li>{n("Je ziet bezorg- en servicekosten voordat je betaalt.","You see delivery and service fees before you pay.")}</li>
<li>{n("Filter op allergenen (bijvoorbeeld zonder gluten of noten). Twijfel je? Vraag het altijd ook aan het restaurant.","Filter by allergens (for example gluten- or nut-free). In doubt? Always check with the restaurant too.")}</li>
<li>{n("Volg je bezorger live op de kaart.","Follow your rider live on the map.")}</li>
<li>{n("Liever zelf ophalen? Dat kan ook, zonder bezorgkosten.","Prefer to collect? You can, with no delivery fee.")}</li>
<li>{n("Fooi gaat altijd voor 100% naar de bezorger.","Tips always go 100% to the rider.")}</li></ul>
<h2>{n("Prijzen","Prices")}</h2>{FEES(L)}<p>{ORDER(L)}</p></section>"""
    if page == "restaurants":
        return f"""<section class="wrap narrow"><h1>{n("Partner worden van Food Porter","Become a Food Porter partner")}</h1>
<p class="lead">{n("Een lokaal bezorgplatform voor Tilburg, met eerlijke voorwaarden voor restaurants.","A local delivery platform for Tilburg, with fair terms for restaurants.")}</p>
<h2>{n("Commissie","Commission")}</h2><table class="fees"><caption class="sr">{n("Commissie","Commission")}</caption>
<thead><tr><th scope="col">{n("Soort bestelling","Order type")}</th><th scope="col">{n("Commissie","Commission")}</th></tr></thead><tbody>
<tr><td>{n("Bezorging, eerste 3 maanden","Delivery, first 3 months")}</td><td>20%</td></tr>
<tr><td>{n("Bezorging, daarna","Delivery, after that")}</td><td>25%</td></tr>
<tr><td>{n("Afhalen","Pickup")}</td><td>10%</td></tr></tbody></table>
<p class="small">{n("Percentages over de waarde van het eten, exclusief btw. De definitieve voorwaarden staan in de partnerovereenkomst.","Percentages of the food value, excluding VAT. Final terms are set out in the partner agreement.")}</p>
<h2>{n("Wat je krijgt","What you get")}</h2><ul class="checks">
<li>{n("Bezorging door onze eigen, opgeleide bezorgers.","Delivery by our own trained riders.")}</li>
<li>{n("Een eenvoudig bestelscherm voor tablet of telefoon, met geluidsmelding.","A simple order screen for tablet or phone, with sound alerts.")}</li>
<li>{n("Zelf je menu, prijzen, allergenen en openingstijden beheren.","Manage your own menu, prices, allergens and opening hours.")}</li>
<li>{n("Overzichtelijke rapporten en uitbetalingen.","Clear reports and payouts.")}</li>
<li>{n("Lokaal contact: we zitten in Tilburg.","Local contact: we are based in Tilburg.")}</li></ul>
<h2>{n("Aanmelden","Sign up")}</h2><p>{n("Stuur ons een mail met de naam van je restaurant en een contactpersoon. We plannen een kennismaking en maken je account aan. Ben je al partner? Log dan in op het restaurantscherm.","Email us your restaurant's name and a contact person. We'll arrange an introduction and set up your account. Already a partner? Sign in to the restaurant screen.")}</p>
<p class="ctas">{btn("mailto:partners@foodporter.nl?subject=" + n("Aanmelding%20restaurant","Restaurant%20sign-up"), n("Meld je restaurant aan","Sign up your restaurant"))} {btn(APP + "/restaurant/", n("Inloggen restaurant","Restaurant sign-in"), "btn btn-alt")}</p></section>"""
    if page == "riders":
        return f"""<section class="wrap narrow"><h1>{n("Werken als bezorger","Work as a rider")}</h1>
<p class="lead" lang="ro"><em>Timpul tău, regulile tale, câștigurile tale</em> <span lang="{n('nl','en')}">— {n("jouw tijd, jouw regels, jouw verdiensten.","your time, your rules, your earnings.")}</span></p>
<ul class="checks"><li>{n("Je komt bij ons in dienst: geen schijnzelfstandigheid.","You are employed by us directly: no bogus self-employment.")}</li>
<li>{n("Loon volgens de toepasselijke cao, inclusief toeslagen en pensioenopbouw.","Pay under the applicable collective agreement (CAO), including surcharges and pension.")}</li>
<li>{n("Keuze uit een oproepcontract of een min-maxcontract.","Choose an on-call or a min-max contract.")}</li>
<li>{n("Per bezorging een extra bonus bovenop je uurloon.","An extra bonus per delivery on top of your hourly wage.")}</li>
<li>{n("Fooien gaan voor 100% naar jou.","Tips go 100% to you.")}</li>
<li>{n("Veilig werken: verplichte pauzes en rusttijden worden in de app bewaakt.","Safe work: mandatory breaks and rest periods are checked in the app.")}</li></ul>
<p class="small">{n("Exacte bedragen staan in je arbeidsovereenkomst en in de bezorgersapp.","Exact amounts are in your employment contract and the rider app.")}</p>
<p class="ctas">{btn(APP + "/rider-info/", n("Meer info en aanmelden","More info and apply"))} {btn("mailto:support@foodporter.nl?subject=" + n("Bezorger%20worden","Become%20a%20rider"), n("Mail ons","Email us"), "btn btn-alt")}</p></section>"""
    if page == "about":
        return f"""<section class="wrap narrow"><h1>{n("Over Food Porter","About Food Porter")}</h1>
<p class="lead">{n("Food Porter is een nieuw, lokaal bezorgplatform uit Tilburg.","Food Porter is a new, local delivery platform from Tilburg.")}</p>
<p>{n("We geloven dat bezorging eerlijk kan: voor klanten duidelijke prijzen, voor restaurants een lagere commissie, en voor bezorgers een echt contract. We starten op 1 januari 2027 met een pilot in Tilburg.","We believe delivery can be fair: clear prices for customers, lower commission for restaurants and a real contract for riders. We start a pilot in Tilburg on 1 January 2027.")}</p>
<p>{n("Food Porter is een project van Sonic Jobs V.O.F.","Food Porter is a project powered by Sonic Jobs V.O.F.")}</p>
<h2>{n("Bedrijfsgegevens","Company details")}</h2><dl class="facts">
<dt>{n("Handelsnaam","Trade name")}</dt><dd>Food Porter</dd>
<dt>{n("Onderneming","Company")}</dt><dd>Sonic Jobs V.O.F.</dd>
<dt>KvK</dt><dd>{ph("KvK-nummer volgt","KvK number to follow",L)}</dd>
<dt>{n("Btw-nummer","VAT number")}</dt><dd>{ph("volgt","to follow",L)}</dd>
<dt>{n("Adres","Address")}</dt><dd>{ph("adres volgt","address to follow",L)}, Tilburg</dd></dl></section>"""
    if page == "faq":
        qa = [(n("Wanneer start Food Porter?","When does Food Porter launch?"), n("Op 1 januari 2027 in Tilburg. Tot die tijd draait de app in testmodus.","On 1 January 2027 in Tilburg. Until then the app runs in test mode.")),
              (n("Waar bezorgen jullie?","Where do you deliver?"), n("Bij de start binnen ongeveer 5 km van het centrum van Tilburg. De app controleert je adres.","At launch within about 5 km of Tilburg city centre. The app checks your address.")),
              (n("Wat kost bezorging?","What does delivery cost?"), n("€ 2,49 tot 3 km, € 3,49 voor 3–5 km en € 4,99 voor 5–10 km, plus € 0,99 servicekosten. Afhalen is zonder bezorgkosten.","€2.49 up to 3 km, €3.49 for 3–5 km and €4.99 for 5–10 km, plus a €0.99 service fee. Pickup has no delivery fee.")),
              (n("Hoe kan ik betalen?","How can I pay?"), n("Online in de app, via onze betaalprovider (onder andere iDEAL en kaart).","Online in the app, through our payment provider (including iDEAL and card).")),
              (n("Moet ik een app downloaden?","Do I need to download an app?"), n("Nee. De app werkt in je browser en je kunt hem op je beginscherm zetten.","No. The app works in your browser and you can add it to your home screen.")),
              (n("Krijgt de bezorger mijn fooi?","Does the rider get my tip?"), n("Ja, fooien gaan voor 100% naar de bezorger.","Yes, tips go 100% to the rider.")),
              (n("Ik heb een allergie. Wat nu?","I have an allergy. What now?"), n("Gebruik het allergenenfilter in de app en neem bij twijfel contact op met het restaurant voordat je bestelt.","Use the allergen filter in the app and contact the restaurant before ordering if in doubt.")),
              (n("Hoe verwijder ik mijn account?","How do I delete my account?"), n("Via je account in de app, of mail privacy@foodporter.nl.","From your account in the app, or email privacy@foodporter.nl."))]
        items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in qa)
        return f'<section class="wrap narrow"><h1>{n("Veelgestelde vragen","Frequently asked questions")}</h1>{items}</section>'
    if page == "contact":
        return f"""<section class="wrap narrow"><h1>Contact</h1><dl class="facts">
<dt>{n("Klantenservice","Customer support")}</dt><dd><a href="mailto:support@foodporter.nl">support@foodporter.nl</a></dd>
<dt>{n("Restaurants","Restaurants")}</dt><dd><a href="mailto:partners@foodporter.nl">partners@foodporter.nl</a></dd>
<dt>{n("Privacy","Privacy")}</dt><dd><a href="mailto:privacy@foodporter.nl">privacy@foodporter.nl</a></dd>
<dt>{n("Onderneming","Company")}</dt><dd>Sonic Jobs V.O.F.</dd>
<dt>{n("Adres","Address")}</dt><dd>{ph("adres volgt","address to follow",L)}, Tilburg</dd>
<dt>KvK</dt><dd>{ph("KvK-nummer volgt","KvK number to follow",L)}</dd></dl>
<p>{n("Heb je een vraag over een bestelling? Gebruik dan de chat bij je bestelling in de app, dan hebben we meteen alle gegevens.","Question about an order? Use the chat on your order in the app so we have all the details right away.")}</p></section>"""
    if page == "legal":
        docs = [(n("Privacyverklaring","Privacy statement"), "/privacy/"), (n("Algemene voorwaarden","Terms and conditions"), "/terms/"),
                (n("Cookieverklaring","Cookie statement"), "/cookies/"), (n("Toegankelijkheidsverklaring","Accessibility statement"), "/accessibility/")]
        li = "".join(f'<li><a href="{APP}{p}">{t}</a></li>' for t, p in docs)
        return f"""<section class="wrap narrow"><h1>{n("Juridisch","Legal")}</h1>
<p class="note">{n("Let op: deze documenten zijn concepten en worden nog beoordeeld door een Nederlandse advocaat.","Please note: these documents are drafts pending review by a Dutch lawyer.")}</p><ul class="links">{li}</ul>
<h2>{n("Deze website","This website")}</h2><p>{n("Deze website gebruikt geen tracking- of advertentiecookies en verzamelt geen persoonsgegevens. De hosting (GitHub Pages) kan technische gegevens zoals je IP-adres kort verwerken om de site te leveren.","This website uses no tracking or advertising cookies and collects no personal data. The host (GitHub Pages) may briefly process technical data such as your IP address to serve the site.")}</p></section>"""

META = {
 "home": (("Food Porter – eten bezorgd in Tilburg","Lokale restaurants, eerlijk bezorgd door bezorgers in dienst. Start 1 januari 2027 in Tilburg."),("Food Porter – food delivery in Tilburg","Local restaurants, delivered fairly by employed riders. Launching 1 January 2027 in Tilburg.")),
 "customers": (("Bestellen – Food Porter","Duidelijke prijzen, allergenenfilter en live volgen."),("Ordering – Food Porter","Clear prices, allergen filter and live tracking.")),
 "restaurants": (("Voor restaurants – Food Porter","Partner worden: 20% commissie de eerste 3 maanden, 10% bij afhalen."),("For restaurants – Food Porter","Become a partner: 20% commission for the first 3 months, 10% for pickup.")),
 "riders": (("Werken als bezorger – Food Porter","In dienst, cao, pensioen en 100% van je fooien."),("Work as a rider – Food Porter","Employed, collective agreement, pension and 100% of your tips.")),
 "about": (("Over ons – Food Porter","Een lokaal bezorgplatform uit Tilburg."),("About – Food Porter","A local delivery platform from Tilburg.")),
 "faq": (("Veelgestelde vragen – Food Porter","Antwoorden over bezorging, prijzen en betalen."),("FAQ – Food Porter","Answers about delivery, prices and payment.")),
 "contact": (("Contact – Food Porter","Neem contact op met Food Porter."),("Contact – Food Porter","Get in touch with Food Porter.")),
 "legal": (("Juridisch – Food Porter","Privacy, voorwaarden, cookies en toegankelijkheid."),("Legal – Food Porter","Privacy, terms, cookies and accessibility.")),
}

def layout(L, title, desc, content, path, alt_path, extra_head=""):
    n = lambda a, b: (a, b)[L]
    lang = n("nl", "en")
    nav = "".join(f'<li><a href="{PAGES[k][L]}"{" aria-current=\"page\"" if PAGES[k][L]==path else ""}>{T[k][L]}</a></li>' for k in NAV)
    alt = f'<link rel="alternate" hreflang="nl" href="{BASE}{alt_path[0]}"><link rel="alternate" hreflang="en" href="{BASE}{alt_path[1]}"><link rel="alternate" hreflang="x-default" href="{BASE}{alt_path[0]}">' if alt_path else ""
    sw = alt_path[1 - L] if alt_path else n("/en/", "/")
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{BASE}{path}">{alt}
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{BASE}{path}"><meta property="og:image" content="{BASE}/assets/og.png"><meta property="og:locale" content="{n('nl_NL','en_GB')}"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#9b0708"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/assets/icon-192.png"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/site.css">{extra_head}</head><body>
<a class="skip" href="#main">{n("Naar de inhoud","Skip to content")}</a>
<header class="top"><div class="wrap top-in"><a class="brand" href="{PAGES['home'][L]}"><img src="/assets/mark.png" width="48" height="32" alt=""><span>Food Porter</span></a>
<nav aria-label="{n('Hoofdmenu','Main menu')}"><ul>{nav}</ul></nav>
<div class="tools"><a class="lang" href="{sw}" hreflang="{n('en','nl')}" lang="{n('en','nl')}">{n("English","Nederlands")}</a> <a class="btn btn-sm" href="{APP}/">{n("Bestellen","Order")}</a></div></div></header>
<main id="main">{content}</main>
<footer class="foot"><div class="wrap foot-in"><div><b>Food Porter</b><br>Tilburg · {n("start 1 januari 2027","launching 1 January 2027")}<br>KvK {ph("volgt","to follow",L)}</div>
<ul><li><a href="{PAGES['legal'][L]}">{T['legal'][L]}</a></li><li><a href="{APP}/privacy/">{n("Privacy","Privacy")}</a></li><li><a href="{APP}/terms/">{n("Voorwaarden","Terms")}</a></li><li><a href="{APP}/cookies/">Cookies</a></li><li><a href="{APP}/accessibility/">{n("Toegankelijkheid","Accessibility")}</a></li></ul>
<ul><li><a href="{PAGES['contact'][L]}">Contact</a></li><li><a href="{PAGES['faq'][L]}">FAQ</a></li><li><a href="{APP}/">{n("Naar de app","Open the app")}</a></li></ul></div>
<p class="wrap small">{n("Een project van Sonic Jobs V.O.F.","Powered by Sonic Jobs V.O.F.")} · {n("Geen tracking-cookies op deze site.","No tracking cookies on this site.")}</p></footer></body></html>"""

def write(path, s):
    p = os.path.join(ROOT, path.strip("/"), "index.html") if not path.endswith(".html") else os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w").write(s)

urls = []
for k, paths in PAGES.items():
    for L in (0, 1):
        t, d = META[k][L]
        write(paths[L], layout(L, t, d, body(k, L), paths[L], paths)); urls.append(paths[L])
# 404 with fallback: old app path /foodporter-app/* -> app.foodporter.nl/*
fallback = """<script>(function(){var p=location.pathname,A='https://app.foodporter.nl',q=location.search+location.hash;if(p.indexOf('/foodporter-app')===0){location.replace(A+(p.slice(15)||'/')+q);return;}var s=p.split('/')[1];if(/^(login|cart|checkout|order|orders|my-orders|admin|rider|rider-info|restaurant|group|r|support|welcome|privacy|terms|cookies|accessibility|offline|legal|reset-password|account)$/.test(s)){location.replace(A+p+q);}})();</script>"""
nf = '<section class="wrap narrow"><h1>Pagina niet gevonden · Page not found</h1><p>Deze pagina bestaat niet (meer). · This page does not exist.</p><p class="ctas"><a class="btn" href="/">Naar de homepage</a> <a class="btn btn-alt" href="/en/">Go to the homepage</a></p></section>'
write("/404.html", layout(0, "Niet gevonden – Food Porter", "Pagina niet gevonden.", nf, "/404.html", None, fallback + '<meta name="robots" content="noindex">'))
write("/foodporter-app/", '<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>Food Porter app</title>' + fallback + '<meta http-equiv="refresh" content="0;url=https://app.foodporter.nl/"><link rel="canonical" href="https://app.foodporter.nl/"><meta name="robots" content="noindex"></head><body><p><a href="https://app.foodporter.nl/">Naar de app · Open the app</a></p></body></html>')
today = datetime.date.today().isoformat()
open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{BASE}{u}</loc><lastmod>{today}</lastmod></url>" for u in urls) + "</urlset>\n")
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
open(os.path.join(ROOT, "CNAME"), "w").write("foodporter.nl\n")
open(os.path.join(ROOT, ".nojekyll"), "w").write("")
print("built", len(urls), "pages")
