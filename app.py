import random
import streamlit as st

st.set_page_config(
    page_title="Læs op til Matematik A med mig",
    page_icon="📘",
    layout="wide",
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(180deg, #f7f9fc 0%, #eef4ff 100%);
    }

    .hero {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 45%, #60a5fa 100%);
        padding: 2.2rem 2rem;
        border-radius: 24px;
        color: white;
        box-shadow: 0 10px 30px rgba(37, 99, 235, 0.18);
        margin-bottom: 1rem;
    }

    .hero h1 {
        margin: 0;
        font-size: 2.2rem;
        line-height: 1.2;
    }

    .hero p {
        margin-top: 0.7rem;
        font-size: 1.05rem;
        opacity: 0.95;
    }

    .pill-row {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-top: 1rem;
    }

    .pill {
        background: rgba(255,255,255,0.16);
        border: 1px solid rgba(255,255,255,0.22);
        padding: 0.45rem 0.8rem;
        border-radius: 999px;
        font-size: 0.92rem;
    }

    .card {
        background: white;
        padding: 1.2rem 1.1rem;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.07);
        border: 1px solid #e5e7eb;
        margin-bottom: 1rem;
    }

    .card h3 {
        margin-top: 0;
        margin-bottom: 0.4rem;
        color: #0f172a;
    }

    .muted {
        color: #475569;
        font-size: 0.98rem;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.8rem;
        margin-top: 0.5rem;
    }

    .small-badge {
        display: inline-block;
        background: #dbeafe;
        color: #1d4ed8;
        border-radius: 999px;
        padding: 0.28rem 0.65rem;
        font-size: 0.82rem;
        font-weight: 600;
        margin-bottom: 0.6rem;
    }

    .score-box {
        background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
        color: #166534;
        border: 1px solid #86efac;
        padding: 1rem 1.1rem;
        border-radius: 18px;
        font-weight: 600;
    }

    .review-item {
        background: white;
        border-left: 5px solid #2563eb;
        padding: 0.9rem 1rem;
        border-radius: 14px;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.05);
        margin-bottom: 0.7rem;
    }

    .stButton > button {
        border-radius: 12px;
        border: none;
        padding: 0.6rem 1rem;
        font-weight: 600;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #eff6ff;
        border-radius: 12px;
        padding: 10px 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# DATA
# =========================================================
MATH_DATA = {
    "Matematik C": {
        "Lineære funktioner": {
            "hvad_er_det": (
                "En lineær funktion viser en ret linje i koordinatsystemet. "
                "Den bruges til at beskrive sammenhænge, der vokser eller falder med et fast beløb."
            ),
            "formler": [
                "f(x) = ax + b",
                "a = hældningskoefficient",
                "b = skæring med y-aksen",
                "a = (y₂ - y₁) / (x₂ - x₁)",
                "Nulpunkt: x = -b / a",
            ],
            "trin": [
                "Beregn a med formlen a = (y₂ - y₁) / (x₂ - x₁).",
                "Skriv y = ax + b og indsæt ét af punkterne.",
                "Isolér b.",
                "Skriv den endelige forskrift: f(x) = ax + b.",
            ],
            "mundtlig": (
                "Lineære funktioner beskriver konstant vækst. "
                "Hældningskoefficienten a fortæller, hvor meget y ændrer sig, når x stiger med 1. "
                "Startværdien b er funktionsværdien, når x er nul."
            ),
            "fejl": [
                "Glemmer minus-tegnet i nulpunktet.",
                "Bytter om på tæller og nævner i hældningsformlen.",
                "Finder a korrekt, men glemmer at beregne b bagefter.",
            ],
            "quiz": [
                {
                    "question": "Hvad er hældningen i funktionen f(x) = 4x + 7?",
                    "answer": "4",
                    "alternatives": [],
                    "explanation": "I f(x) = ax + b er hældningen tallet foran x. Her er a = 4.",
                },
                {
                    "question": "Hvad er skæringen med y-aksen i f(x) = -3x + 9?",
                    "answer": "9",
                    "alternatives": [],
                    "explanation": "I f(x) = ax + b er b skæringen med y-aksen. Her er b = 9.",
                },
                {
                    "question": "Bestem f(2), når f(x) = 3x + 1.",
                    "answer": "7",
                    "alternatives": [],
                    "explanation": "Indsæt x = 2: f(2) = 3·2 + 1 = 7.",
                },
            ],
        },
        "Eksponentielle funktioner": {
            "hvad_er_det": (
                "En eksponentiel funktion bruges til at beskrive procentvis vækst eller fald. "
                "Her ændrer y sig med en fast procentdel, ikke et fast beløb."
            ),
            "formler": [
                "f(x) = b · a^x",
                "b = startværdi",
                "a = fremskrivningsfaktor",
                "a^x = b → x = ln(b) / ln(a)",
                "Fordoblingskonstant: T₂ = ln(2) / ln(a)",
                "Halveringskonstant: T½ = ln(0,5) / ln(a)",
            ],
            "trin": [
                "Skriv to ligninger ud fra to punkter.",
                "Divider ligningerne for at isolere a.",
                "Tag ln på begge sider for at finde a.",
                "Indsæt a i en af ligningerne og find b.",
            ],
            "mundtlig": (
                "Eksponentiel vækst betyder, at funktionen vokser med den samme procent i hvert interval. "
                "Fremskrivningsfaktoren a angiver, hvad der sker med y, når x stiger med 1."
            ),
            "fejl": [
                "Glemmer at tage ln på begge sider.",
                "Bytter tæller og nævner i ln-brøken.",
                "Forveksler a og b.",
            ],
            "quiz": [
                {
                    "question": "Hvad er startværdien i f(x) = 5 · 1.2^x?",
                    "answer": "5",
                    "alternatives": [],
                    "explanation": "I f(x)=b·a^x er startværdien b. Her er b = 5.",
                },
                {
                    "question": "Er der vækst eller fald i f(x) = 2 · 0.8^x?",
                    "answer": "fald",
                    "alternatives": ["aftagende"],
                    "explanation": "Når 0 < a < 1, er der eksponentielt fald.",
                },
            ],
        },
        "Rentesregning & annuiteter": {
            "hvad_er_det": (
                "Rentesregning handler om, hvordan penge vokser over tid med rente. "
                "Annuiteter er faste indbetalinger eller afdrag."
            ),
            "formler": [
                "Kₙ = K₀ · (1 + r)^n",
                "r = (Kₙ / K₀)^(1/n) - 1",
                "A = y · ((1 + r)^n - 1) / r",
                "y = K₀ · r / (1 - (1 + r)^(-n))",
            ],
            "trin": [
                "Identificér startkapital, rente og antal perioder.",
                "Omregn procent til decimal.",
                "Vælg korrekt formel: opsparing eller lån.",
                "Indsæt tallene og beregn.",
            ],
            "mundtlig": (
                "Rentesregning er en eksponentiel model, fordi kapitalen vokser med en fast procentdel per periode. "
                "Annuitetsformlen bruges ved faste indbetalinger eller faste afdrag."
            ),
            "fejl": [
                "Glemmer at omregne procent til decimal.",
                "Blander antal måneder og år i n.",
                "Bruger forkert formel for opsparing og lån.",
            ],
            "quiz": [
                {
                    "question": "Skriv 5% som decimaltal.",
                    "answer": "0.05",
                    "alternatives": ["0,05"],
                    "explanation": "5% = 5/100 = 0,05.",
                },
                {
                    "question": "Hvad er startkapitalen i formlen Kₙ = K₀ · (1+r)^n?",
                    "answer": "k₀",
                    "alternatives": ["k0", "K0", "K₀"],
                    "explanation": "K₀ er startkapitalen.",
                },
            ],
        },
        "Deskriptiv statistik": {
            "hvad_er_det": (
                "Statistik beskriver og opsummerer data. "
                "De vigtigste mål er middelværdi, varians, spredning og kvartiler."
            ),
            "formler": [
                "Middelværdi: x̄ = Σx / n",
                "Varians: s² = Σ(x - x̄)² / n",
                "Spredning: s = √s²",
                "Q1 = 25%, Q2 = median, Q3 = 75%",
            ],
            "trin": [
                "Beregn middelværdien.",
                "Find afvigelserne fra middelværdien.",
                "Kvadrér afvigelserne og find variansen.",
                "Tag kvadratroden for at finde spredningen.",
            ],
            "mundtlig": (
                "Middelværdien angiver centrum af datasættet. "
                "Spredningen fortæller, hvor tæt observationerne ligger på middelværdien."
            ),
            "fejl": [
                "Glemmer at kvadrere afvigelserne i variansen.",
                "Tager ikke kvadratroden for at finde spredningen.",
            ],
            "quiz": [
                {
                    "question": "Hvad kaldes gennemsnittet i statistik?",
                    "answer": "middelværdi",
                    "alternatives": ["gennemsnit"],
                    "explanation": "Middelværdi er det samme som gennemsnit.",
                },
                {
                    "question": "Hvad er medianen også kaldet i kvartiler?",
                    "answer": "q2",
                    "alternatives": ["Q2", "2. kvartil", "anden kvartil"],
                    "explanation": "Medianen er Q2.",
                },
            ],
        },
        "Andengradspolynomier": {
            "hvad_er_det": (
                "En andengradsfunktion er en parabel. "
                "Den kan have nul, ét eller to nulpunkter og har ét toppunkt eller bundpunkt."
            ),
            "formler": [
                "f(x) = ax² + bx + c",
                "d = b² - 4ac",
                "x = (-b ± √d) / (2a)",
                "x_T = -b / (2a)",
            ],
            "trin": [
                "Identificér a, b og c.",
                "Beregn diskriminanten d.",
                "Brug nulpunktsformlen.",
                "Find toppunktet ved x_T = -b/(2a).",
            ],
            "mundtlig": (
                "Diskriminanten afgør, hvor mange nulpunkter parablen har. "
                "Toppunktet er parablens ekstremum."
            ),
            "fejl": [
                "Glemmer minus foran b i nulpunktsformlen.",
                "Glemmer ± i formlen.",
                "Beregner diskriminanten forkert.",
            ],
            "quiz": [
                {
                    "question": "Hvor mange nulpunkter har en andengradsfunktion, hvis d > 0?",
                    "answer": "2",
                    "alternatives": ["to"],
                    "explanation": "Hvis diskriminanten er positiv, er der to nulpunkter.",
                },
                {
                    "question": "Hvad er diskriminanten for ax² + bx + c?",
                    "answer": "b² - 4ac",
                    "alternatives": ["b^2 - 4ac", "b2 - 4ac"],
                    "explanation": "Diskriminanten er d = b² - 4ac.",
                },
            ],
        },
    },
    "Matematik B": {
        "Differentialregning": {
            "hvad_er_det": (
                "Differentialregning handler om ændringshastighed. "
                "Den afledte funktion fortæller, hvor hurtigt funktionen stiger eller falder."
            ),
            "formler": [
                "(x^n)' = n · x^(n-1)",
                "(e^x)' = e^x",
                "(a^x)' = a^x · ln(a)",
                "(ln x)' = 1/x",
                "Produktregel: (u·v)' = u'·v + u·v'",
                "Kæderegel: f(g(x))' = f'(g(x)) · g'(x)",
                "Tangent: y = f'(x₀)(x - x₀) + f(x₀)",
            ],
            "trin": [
                "Find definitionsmængden.",
                "Find nulpunkter ved at løse f(x)=0.",
                "Differentier og find f'(x).",
                "Sæt f'(x)=0 for at finde mulige ekstrema.",
                "Undersøg, hvor funktionen er stigende og faldende.",
            ],
            "mundtlig": (
                "Den afledte måler hældningen af tangenten i et punkt. "
                "Når f'(x)=0, kan der være et lokalt maksimum eller minimum."
            ),
            "fejl": [
                "Sætter ikke f'(x)=0 for at finde ekstrema.",
                "Differentierer x^n forkert.",
                "Glemmer kædereglen ved sammensatte funktioner.",
            ],
            "quiz": [
                {
                    "question": "Differentiér f(x)=x².",
                    "answer": "2x",
                    "alternatives": ["2*x"],
                    "explanation": "Ved potensreglen bliver den afledte af x² til 2x.",
                },
                {
                    "question": "Differentiér f(x)=7x-3.",
                    "answer": "7",
                    "alternatives": [],
                    "explanation": "Den afledte af ax+b er a.",
                },
            ],
        },
        "Lineær programmering": {
            "hvad_er_det": (
                "Lineær programmering bruges til at optimere under begrænsninger. "
                "Løsningen findes i et hjørnepunkt i det tilladte område."
            ),
            "formler": [
                "Maksimér/minimér: Z = ax + by",
                "Bibetingelser: a₁x + b₁y ≤ c₁",
                "Samt x ≥ 0, y ≥ 0",
            ],
            "trin": [
                "Definér variable.",
                "Opskriv bibetingelser som uligheder.",
                "Tegn linjerne og markér det gyldige område.",
                "Find hjørnepunkterne.",
                "Test alle hjørnepunkter i målfunktionen.",
            ],
            "mundtlig": (
                "I lineær programmering tester man hjørnepunkterne, fordi det optimale punkt altid ligger i et hjørnepunkt."
            ),
            "fejl": [
                "Bruger lighed i stedet for ulighed.",
                "Tester ikke alle hjørnepunkter.",
                "Tegner det forkerte område.",
            ],
            "quiz": [
                {
                    "question": "Hvor ligger den optimale løsning i lineær programmering typisk?",
                    "answer": "hjørnepunkt",
                    "alternatives": ["et hjørnepunkt", "i et hjørnepunkt"],
                    "explanation": "Det optimale punkt findes i et hjørnepunkt.",
                },
                {
                    "question": "Skal man teste alle hjørnepunkter? (ja/nej)",
                    "answer": "ja",
                    "alternatives": [],
                    "explanation": "Ja, alle hjørnepunkter skal testes.",
                },
            ],
        },
        "Sandsynlighedsregning": {
            "hvad_er_det": (
                "Sandsynlighedsregning beskriver, hvor sandsynligt et udfald er. "
                "Binomialfordelingen bruges ved uafhængige forsøg med to mulige udfald."
            ),
            "formler": [
                "P(A) = antal gunstige / antal mulige",
                "P(X = k) = C(n,k) · p^k · (1-p)^(n-k)",
                "μ = n · p",
                "σ² = n · p · (1-p)",
                "Z = (x - μ) / σ",
            ],
            "trin": [
                "Afgør hvilken model der passer til opgaven.",
                "Bestem n, k og p ved binomialfordeling.",
                "Indsæt korrekt i formlen.",
                "Brug evt. normalfordeling ved store stikprøver.",
            ],
            "mundtlig": (
                "Binomialfordelingen kræver n uafhængige forsøg og konstant sandsynlighed p for succes."
            ),
            "fejl": [
                "Forveksler n og k.",
                "Bruger forkert model.",
                "Glemmer parenteser i (1-p)^(n-k).",
            ],
            "quiz": [
                {
                    "question": "En fair terning kastes én gang. Hvad er sandsynligheden for en 6'er?",
                    "answer": "1/6",
                    "alternatives": ["0.1667", "0,1667", "0.167", "0,167"],
                    "explanation": "Der er 1 gunstigt udfald ud af 6 mulige.",
                },
                {
                    "question": "Hvad står n for i binomialfordelingen?",
                    "answer": "antal forsøg",
                    "alternatives": [],
                    "explanation": "n er antallet af forsøg.",
                },
            ],
        },
        "Konfidensinterval & hypotesetest": {
            "hvad_er_det": (
                "Konfidensintervaller giver et sandsynligt interval for en ukendt parameter. "
                "Hypotesetest bruges til at vurdere, om data er statistisk signifikante."
            ),
            "formler": [
                "For andel: p̂ ± 1,96 · √(p̂(1-p̂)/n)",
                "For middelværdi: x̄ ± 1,96 · s/√n",
                "Z = (x̄ - μ₀) / (s/√n)",
                "p-værdi < 0,05 → forkast H₀",
            ],
            "trin": [
                "Find ud af om det er andel eller middelværdi.",
                "Vælg den rigtige formel.",
                "Beregn interval eller teststørrelse.",
                "Sammenlign p-værdi med signifikansniveauet.",
            ],
            "mundtlig": (
                "Et 95% konfidensinterval angiver et interval, hvor den sande parameter forventes at ligge. "
                "I hypotesetest vurderer man, om nulhypotesen kan forkastes."
            ),
            "fejl": [
                "Bruger andelsformlen ved middelværdi og omvendt.",
                "Glemmer √n i nævneren.",
                "Tolker p < 0,05 forkert.",
            ],
            "quiz": [
                {
                    "question": "Hvad gør man typisk, hvis p-værdi < 0,05?",
                    "answer": "forkast h0",
                    "alternatives": ["forkast H0", "forkaster h0", "forkaster H0"],
                    "explanation": "Når p-værdien er mindre end 0,05, forkaster man nulhypotesen.",
                },
                {
                    "question": "Er 1,96 en typisk kritisk værdi ved 95% konfidensinterval? (ja/nej)",
                    "answer": "ja",
                    "alternatives": [],
                    "explanation": "Ja, 1,96 bruges ofte ved 95%.",
                },
            ],
        },
    },
    "Matematik A": {
        "Integralregning": {
            "hvad_er_det": (
                "Integration er omvendt differentiation. "
                "Det bruges til at finde arealer under grafer og stamfunktioner."
            ),
            "formler": [
                "∫ x^n dx = x^(n+1)/(n+1) + C",
                "∫ e^x dx = e^x + C",
                "∫ a^x dx = a^x / ln(a) + C",
                "∫ 1/x dx = ln|x| + C",
                "∫ₐᵇ f(x) dx = F(b) - F(a)",
                "A = ∫ₐᵇ (f(x) - g(x)) dx",
                "Partiel integration: ∫u·v' dx = u·v - ∫u'·v dx",
            ],
            "trin": [
                "Find stamfunktionen F(x).",
                "Beregn F(b) og F(a).",
                "Træk fra: F(b) - F(a).",
                "Ved areal mellem grafer: øverste funktion minus nederste funktion.",
            ],
            "mundtlig": (
                "Integration er den omvendte proces af differentiation. "
                "Det bestemte integral beregnes som F(b) - F(a)."
            ),
            "fejl": [
                "Glemmer +C ved ubestemte integraler.",
                "Beregner F(a)-F(b) i stedet for F(b)-F(a).",
                "Glemmer at trække nederste funktion fra.",
            ],
            "quiz": [
                {
                    "question": "Bestem ∫ 2x dx.",
                    "answer": "x^2 + c",
                    "alternatives": ["x² + c", "x^2+c", "x²+c"],
                    "explanation": "Stamfunktionen til 2x er x² + C.",
                },
                {
                    "question": "Hvad er reglen for et bestemt integral?",
                    "answer": "F(b) - F(a)",
                    "alternatives": ["f(b)-f(a)", "F(b)-F(a)"],
                    "explanation": "Det bestemte integral beregnes som F(b) - F(a).",
                },
            ],
        },
        "Differentialligninger": {
            "hvad_er_det": (
                "En differentialligning indeholder en funktion og dens afledte. "
                "Den bruges til at modellere processer som vækst og afkøling."
            ),
            "formler": [
                "y' = k · y",
                "y = C · e^(kx)",
                "Logistisk vækst: y' = k · y · (M - y)",
            ],
            "trin": [
                "Identificér typen af differentialligning.",
                "Brug den kendte løsningsform.",
                "Bestem konstanten C ud fra begyndelsesværdien.",
                "Eftervis evt. løsningen ved at differentiere og indsætte.",
            ],
            "mundtlig": (
                "Differentialligningen y' = ky betyder, at vækstraten er proportional med den nuværende størrelse. "
                "Det giver eksponentiel vækst."
            ),
            "fejl": [
                "Glemmer integrationskonstanten C.",
                "Bestemmer ikke C ud fra begyndelsesværdien.",
                "Forveksler eksponentiel og logistisk model.",
            ],
            "quiz": [
                {
                    "question": "Hvad er løsningen til y' = k·y?",
                    "answer": "c·e^(kx)",
                    "alternatives": ["C·e^(kx)", "Ce^(kx)", "c e^(kx)", "C e^(kx)"],
                    "explanation": "Den generelle løsning er y = C·e^(kx).",
                },
                {
                    "question": "Hvad står M for i logistisk vækst?",
                    "answer": "bærekapacitet",
                    "alternatives": [],
                    "explanation": "M er bærekapaciteten, altså den maksimale størrelse.",
                },
            ],
        },
        "Trigonometriske funktioner": {
            "hvad_er_det": (
                "Trigonometri beskriver svingninger og cykliske fænomener. "
                "Den harmoniske svingning er vigtig til eksamen."
            ),
            "formler": [
                "sin²(x) + cos²(x) = 1",
                "f(x) = A · sin(Bx + C) + D",
                "T = 2π / B",
                "sin(0)=0, sin(π/2)=1, sin(π)=0",
                "cos(0)=1, cos(π/2)=0, cos(π)=-1",
            ],
            "trin": [
                "Identificér A, B, C og D i funktionen.",
                "Find amplituden ud fra A.",
                "Find perioden med T = 2π/B.",
                "Bestem evt. faseforskydning og midterlinje.",
            ],
            "mundtlig": (
                "Amplituden angiver den maksimale afvigelse fra midterlinjen. "
                "Perioden er den tid, det tager at gennemføre én fuld svingning."
            ),
            "fejl": [
                "Blander grader og radianer.",
                "Beregner perioden som 2π·B i stedet for 2π/B.",
                "Forveksler amplitude og periode.",
            ],
            "quiz": [
                {
                    "question": "Hvad er perioden for f(x)=A·sin(2x+C)+D?",
                    "answer": "pi",
                    "alternatives": ["π", "3.14159"],
                    "explanation": "T = 2π/B = 2π/2 = π.",
                },
                {
                    "question": "Hvad er amplituden i f(x)=3·sin(x)+2?",
                    "answer": "3",
                    "alternatives": [],
                    "explanation": "Amplituden er |A|, altså 3.",
                },
            ],
        },
        "Vektorer": {
            "hvad_er_det": (
                "En vektor har både retning og størrelse. "
                "Vektorer bruges i geometri og fysik til at beskrive bevægelse og sammenhænge."
            ),
            "formler": [
                "a⃗ = (x, y)",
                "|a⃗| = √(x² + y²)",
                "a⃗ + b⃗ = (x₁+x₂, y₁+y₂)",
                "a⃗ · b⃗ = x₁x₂ + y₁y₂",
                "cos(v) = (a⃗ · b⃗) / (|a⃗| · |b⃗|)",
                "Ortogonale vektorer: a⃗ · b⃗ = 0",
                "Areal: A = |x₁y₂ - x₂y₁|",
            ],
            "trin": [
                "Læs koordinaterne for vektorerne.",
                "Brug den rigtige formel til længde, sum eller prikprodukt.",
                "Ved vinkel: brug cosinus-formlen.",
                "Ved ortogonalitet: tjek om prikproduktet er 0.",
            ],
            "mundtlig": (
                "Prikproduktet kombinerer to vektorer til et tal. "
                "Hvis prikproduktet er nul, er vektorerne ortogonale."
            ),
            "fejl": [
                "Glemmer kvadratroden i længdeformlen.",
                "Forveksler addition og prikprodukt.",
                "Blander radianer og grader i vinkelopgaver.",
            ],
            "quiz": [
                {
                    "question": "Hvad er længden af vektoren (3,4)?",
                    "answer": "5",
                    "alternatives": [],
                    "explanation": "Længden er √(3² + 4²) = √25 = 5.",
                },
                {
                    "question": "Hvad er prikproduktet af (1,2) og (3,4)?",
                    "answer": "11",
                    "alternatives": [],
                    "explanation": "1·3 + 2·4 = 3 + 8 = 11.",
                },
            ],
        },
        "Keglesnit": {
            "hvad_er_det": (
                "Keglesnit er geometriske kurver som fx cirkler og ellipser. "
                "De vigtigste til eksamen er cirkel og ellipse."
            ),
            "formler": [
                "(x - h)² + (y - k)² = r²",
                "(x - h)²/a² + (y - k)²/b² = 1",
            ],
            "trin": [
                "Aflæs standardformen.",
                "Find centrum og radius eller halvakser.",
                "Ved omskrivning: fuldend kvadratet for x og y separat.",
            ],
            "mundtlig": (
                "En cirkel er et specialtilfælde af ellipsen, hvor halvakserne er lige store."
            ),
            "fejl": [
                "Forveksler centrum med fortegnene.",
                "Aflæser radius som r² i stedet for r.",
            ],
            "quiz": [
                {
                    "question": "Hvad er radius i ligningen (x-1)² + (y+2)² = 9?",
                    "answer": "3",
                    "alternatives": [],
                    "explanation": "Radius er kvadratroden af 9, altså 3.",
                },
                {
                    "question": "Er en cirkel et specialtilfælde af en ellipse? (ja/nej)",
                    "answer": "ja",
                    "alternatives": [],
                    "explanation": "Ja, når halvakserne er lige store.",
                },
            ],
        },
    },
}

QUICK_REVIEW = {
    "Matematik C": [
        "Lineær funktion: f(x)=ax+b",
        "Eksponentiel funktion: f(x)=b·a^x",
        "Renteformel: Kₙ = K₀·(1+r)^n",
        "Middelværdi: x̄ = Σx/n",
        "Diskriminant: d = b² - 4ac",
    ],
    "Matematik B": [
        "Potensregel: (x^n)' = n·x^(n-1)",
        "Produktregel og kæderegel",
        "Lineær programmering: test hjørnepunkter",
        "Binomialfordeling: P(X=k)=C(n,k)p^k(1-p)^(n-k)",
        "p-værdi < 0,05 → forkast H₀",
    ],
    "Matematik A": [
        "Integral: F(b)-F(a)",
        "Stamfunktion: ∫x^n dx = x^(n+1)/(n+1) + C",
        "Differentialligning: y'=ky → y=C·e^(kx)",
        "Trigonometrisk periode: T=2π/B",
        "Prikprodukt: a⃗·b⃗ = x₁x₂ + y₁y₂",
    ],
}
EXAM_TASKS = {
    "Matematik C": {
        "Lineære funktioner": {
            "opgave": (
                "Givet punkterne A(2,5) og B(6,13).\n\n"
                "1. Bestem hældningskoefficienten.\n"
                "2. Bestem forskriften for funktionen.\n"
                "3. Bestem nulpunktet.\n"
                "4. Forklar hvad a og b betyder."
            ),
            "løsningsforslag": (
                "1. a = (13 - 5) / (6 - 2) = 8 / 4 = 2\n"
                "2. Brug y = ax + b. Indsæt punktet (2,5): 5 = 2·2 + b → b = 1\n"
                "   Funktionen er derfor f(x) = 2x + 1\n"
                "3. Nulpunkt: 0 = 2x + 1 → x = -0,5\n"
                "4. a er hældningen, og b er skæringen med y-aksen."
            ),
        },
        "Eksponentielle funktioner": {
            "opgave": (
                "En funktion går gennem punkterne (0,4) og (3,32).\n\n"
                "1. Bestem forskriften f(x)=b·a^x.\n"
                "2. Er der vækst eller fald?\n"
                "3. Bestem fordoblingskonstanten."
            ),
            "løsningsforslag": (
                "1. Når x = 0 fås b = 4.\n"
                "   32 = 4·a^3 → 8 = a^3 → a = 2\n"
                "   Funktionen er f(x) = 4·2^x\n"
                "2. Der er vækst, fordi a > 1.\n"
                "3. Fordoblingskonstant: T₂ = ln(2)/ln(2) = 1"
            ),
        },
        "Rentesregning & annuiteter": {
            "opgave": (
                "Du indsætter 10.000 kr. på en konto med 3% rente i 5 år.\n\n"
                "1. Hvor meget står der efter 5 år?\n"
                "2. Hvor lang tid tager det at fordoble beløbet?"
            ),
            "løsningsforslag": (
                "1. Kₙ = 10000·(1,03)^5 ≈ 11592,74 kr.\n"
                "2. Fordobling: 2 = (1,03)^n\n"
                "   n = ln(2)/ln(1,03) ≈ 23,45 år"
            ),
        },
        "Deskriptiv statistik": {
            "opgave": (
                "Givet datasættet: 4, 6, 8, 10, 12.\n\n"
                "1. Bestem middelværdi.\n"
                "2. Bestem varians.\n"
                "3. Bestem spredning.\n"
                "4. Forklar hvad spredning betyder."
            ),
            "løsningsforslag": (
                "1. Middelværdi: (4+6+8+10+12)/5 = 8\n"
                "2. Varians: ((4-8)^2+(6-8)^2+(8-8)^2+(10-8)^2+(12-8)^2)/5\n"
                "   = (16+4+0+4+16)/5 = 40/5 = 8\n"
                "3. Spredning: √8 ≈ 2,83\n"
                "4. Spredning fortæller, hvor meget tallene ligger spredt omkring gennemsnittet."
            ),
        },
        "Andengradspolynomier": {
            "opgave": (
                "f(x) = x² - 4x + 3\n\n"
                "1. Bestem diskriminanten.\n"
                "2. Find nulpunkterne.\n"
                "3. Find toppunktet.\n"
                "4. Er det et maksimum eller minimum?"
            ),
            "løsningsforslag": (
                "1. a=1, b=-4, c=3\n"
                "   d = (-4)^2 - 4·1·3 = 16 - 12 = 4\n"
                "2. x = (4 ± √4)/2 = (4 ± 2)/2 → x = 1 og x = 3\n"
                "3. x_T = -(-4)/(2·1) = 2\n"
                "   y_T = 2^2 - 4·2 + 3 = -1\n"
                "   Toppunkt: (2, -1)\n"
                "4. Det er et minimum, fordi a > 0."
            ),
        },
    },
    "Matematik B": {
        "Differentialregning": {
            "opgave": (
                "f(x) = x³ - 3x² + 2\n\n"
                "1. Find f'(x).\n"
                "2. Find kritiske punkter.\n"
                "3. Undersøg hvor funktionen er voksende og aftagende.\n"
                "4. Bestem lokale ekstrema."
            ),
            "løsningsforslag": (
                "1. f'(x) = 3x² - 6x = 3x(x-2)\n"
                "2. Kritiske punkter: 3x(x-2)=0 → x=0 og x=2\n"
                "3. Funktionen er voksende for x<0 og x>2, aftagende for 0<x<2\n"
                "4. f(0)=2 og f(2)=-2\n"
                "   Lokalt maksimum i (0,2)\n"
                "   Lokalt minimum i (2,-2)"
            ),
        },
        "Lineær programmering": {
            "opgave": (
                "Maksimér Z = 3x + 2y under betingelserne:\n"
                "x + y ≤ 10\n"
                "x ≥ 0\n"
                "y ≥ 0\n\n"
                "1. Tegn området.\n"
                "2. Find hjørnepunkterne.\n"
                "3. Find maksimal værdi."
            ),
            "løsningsforslag": (
                "1. Området er trekanten i første kvadrant under linjen x+y=10\n"
                "2. Hjørnepunkter: (0,0), (10,0), (0,10)\n"
                "3. Z(0,0)=0\n"
                "   Z(10,0)=30\n"
                "   Z(0,10)=20\n"
                "   Maksimum er 30 i punktet (10,0)"
            ),
        },
        "Sandsynlighedsregning": {
            "opgave": (
                "En mønt kastes 10 gange. Sandsynligheden for plat er 0,5.\n\n"
                "1. Bestem P(X=6).\n"
                "2. Bestem P(X≥6).\n"
                "3. Beregn middelværdi og varians."
            ),
            "løsningsforslag": (
                "1. P(X=6) = C(10,6)·0,5^6·0,5^4 = C(10,6)·0,5^10\n"
                "   = 210/1024 ≈ 0,2051\n"
                "2. P(X≥6) = P(6)+P(7)+P(8)+P(9)+P(10)\n"
                "   = (210+120+45+10+1)/1024 = 386/1024 ≈ 0,3770\n"
                "3. Middelværdi: μ = n·p = 10·0,5 = 5\n"
                "   Varians: σ² = n·p·(1-p) = 10·0,5·0,5 = 2,5"
            ),
        },
        "Konfidensinterval & hypotesetest": {
            "opgave": (
                "I en stikprøve er p̂ = 0,6 og n = 100.\n\n"
                "1. Bestem et 95% konfidensinterval.\n"
                "2. Fortolk intervallet."
            ),
            "løsningsforslag": (
                "1. p̂ ± 1,96·√(p̂(1-p̂)/n)\n"
                "   = 0,6 ± 1,96·√(0,6·0,4/100)\n"
                "   = 0,6 ± 1,96·√0,0024\n"
                "   = 0,6 ± 1,96·0,049\n"
                "   ≈ 0,6 ± 0,096\n"
                "   Interval: [0,504 ; 0,696]\n"
                "2. Den sande andel forventes med 95% sikkerhed at ligge mellem ca. 50,4% og 69,6%."
            ),
        },
    },
    "Matematik A": {
        "Integralregning": {
            "opgave": (
                "f(x)=2x\n\n"
                "1. Bestem en stamfunktion.\n"
                "2. Beregn ∫₀⁴ 2x dx.\n"
                "3. Forklar hvad resultatet betyder geometrisk."
            ),
            "løsningsforslag": (
                "1. En stamfunktion er F(x)=x² + C\n"
                "2. ∫₀⁴ 2x dx = F(4)-F(0) = 4² - 0² = 16\n"
                "3. Resultatet er arealet under grafen for f(x)=2x fra x=0 til x=4."
            ),
        },
        "Differentialligninger": {
            "opgave": (
                "y' = 0,5y\n\n"
                "1. Løs differentialligningen.\n"
                "2. Bestem løsningen når y(0)=4.\n"
                "3. Forklar hvad modellen beskriver."
            ),
            "løsningsforslag": (
                "1. Den generelle løsning er y = C·e^(0,5x)\n"
                "2. y(0)=4 → 4 = C·e^0 = C\n"
                "   Løsningen er y = 4·e^(0,5x)\n"
                "3. Modellen beskriver eksponentiel vækst, fordi vækstraten er proportional med størrelsen."
            ),
        },
        "Trigonometriske funktioner": {
            "opgave": (
                "f(x)=3sin(2x)+1\n\n"
                "1. Bestem amplitude.\n"
                "2. Bestem periode.\n"
                "3. Bestem maksimum og minimum.\n"
                "4. Skitser grafen."
            ),
            "løsningsforslag": (
                "1. Amplituden er 3\n"
                "2. Perioden er T = 2π/2 = π\n"
                "3. Midterlinje er y=1\n"
                "   Maksimum: 1+3 = 4\n"
                "   Minimum: 1-3 = -2\n"
                "4. Grafen svinger omkring y=1 med amplitude 3 og periode π."
            ),
        },
        "Vektorer": {
            "opgave": (
                "a=(2,3), b=(4,1)\n\n"
                "1. Bestem a+b.\n"
                "2. Bestem længden af a.\n"
                "3. Bestem prikproduktet.\n"
                "4. Undersøg om de er ortogonale."
            ),
            "løsningsforslag": (
                "1. a+b = (2+4, 3+1) = (6,4)\n"
                "2. |a| = √(2²+3²) = √13\n"
                "3. a·b = 2·4 + 3·1 = 11\n"
                "4. De er ikke ortogonale, fordi prikproduktet ikke er 0."
            ),
        },
        "Keglesnit": {
            "opgave": (
                "(x-2)² + (y+1)² = 16\n\n"
                "1. Bestem centrum.\n"
                "2. Bestem radius.\n"
                "3. Tegn cirklen.\n"
                "4. Forklar ligningen."
            ),
            "løsningsforslag": (
                "1. Centrum er (2,-1)\n"
                "2. Radius er √16 = 4\n"
                "3. Cirklen tegnes med centrum (2,-1) og radius 4\n"
                "4. Ligningen er standardformen for en cirkel: (x-h)² + (y-k)² = r²"
            ),
        },
    },
}
EXTRA_QUIZ_QUESTIONS = {
    "Matematik C": {
        "Lineære funktioner": [
            {
                "question": "Bestem hældningen for linjen gennem punkterne (1,3) og (5,11).",
                "answer": "2",
                "alternatives": [],
                "explanation": "a = (11-3)/(5-1) = 8/4 = 2.",
            },
            {
                "question": "Bestem forskriften for en lineær funktion med hældning 3 og y-akseskæring -2.",
                "answer": "f(x)=3x-2",
                "alternatives": ["3x-2", "y=3x-2"],
                "explanation": "En lineær funktion skrives som f(x)=ax+b. Her er a=3 og b=-2.",
            },
            {
                "question": "Hvad er nulpunktet for f(x)=5x-15?",
                "answer": "3",
                "alternatives": [],
                "explanation": "Sæt 5x-15=0, så fås x=3.",
            },
            {
                "question": "Er en lineær funktion med a<0 stigende eller faldende?",
                "answer": "faldende",
                "alternatives": [],
                "explanation": "Når a<0, falder grafen fra venstre mod højre.",
            },
            {
                "question": "Hvad betyder b i f(x)=ax+b?",
                "answer": "skæring med y-aksen",
                "alternatives": ["startværdi", "y-akseskæring"],
                "explanation": "b er funktionsværdien når x=0.",
            },
        ],
        "Eksponentielle funktioner": [
            {
                "question": "Hvad er fremskrivningsfaktoren i f(x)=8·1,03^x?",
                "answer": "1,03",
                "alternatives": ["1.03"],
                "explanation": "I f(x)=b·a^x er a fremskrivningsfaktoren.",
            },
            {
                "question": "Hvad er begyndelsesværdien i f(x)=12·0,95^x?",
                "answer": "12",
                "alternatives": [],
                "explanation": "Begyndelsesværdien er b, dvs. f(0)=12.",
            },
            {
                "question": "Er der vækst eller fald når a=1,08?",
                "answer": "vækst",
                "alternatives": [],
                "explanation": "Når a>1, er der eksponentiel vækst.",
            },
            {
                "question": "Hvad bruges ln typisk til i eksponentielle ligninger?",
                "answer": "at isolere x",
                "alternatives": ["isolere eksponenten", "finde x"],
                "explanation": "Logaritmer bruges til at isolere den ukendte eksponent.",
            },
            {
                "question": "Hvad er fordoblingskonstanten for f(x)=b·2^x?",
                "answer": "1",
                "alternatives": [],
                "explanation": "T₂ = ln(2)/ln(2) = 1.",
            },
        ],
        "Rentesregning & annuiteter": [
            {
                "question": "Skriv 7% som decimaltal.",
                "answer": "0.07",
                "alternatives": ["0,07"],
                "explanation": "7% = 7/100 = 0,07.",
            },
            {
                "question": "Hvad betyder n i Kₙ=K₀·(1+r)^n?",
                "answer": "antal perioder",
                "alternatives": ["perioder", "terminer"],
                "explanation": "n er antallet af renteperioder.",
            },
            {
                "question": "Vokser eller falder kapitalen når r er positiv?",
                "answer": "vokser",
                "alternatives": [],
                "explanation": "Positiv rente giver vækst.",
            },
            {
                "question": "Hvad kaldes en opsparing med fast indbetaling hver termin?",
                "answer": "annuitetsopsparing",
                "alternatives": ["annuitet"],
                "explanation": "Ved faste indbetalinger bruges annuitetsopsparing.",
            },
            {
                "question": "Hvad kaldes et lån med fast ydelse hver termin?",
                "answer": "annuitetslån",
                "alternatives": [],
                "explanation": "Et lån med samme betaling hver termin er et annuitetslån.",
            },
        ],
        "Deskriptiv statistik": [
            {
                "question": "Hvad er medianen i datasættet 1, 3, 5, 7, 9?",
                "answer": "5",
                "alternatives": [],
                "explanation": "Medianen er det midterste tal i det sorterede datasæt.",
            },
            {
                "question": "Hvad er middelværdien af 2, 4, 6, 8?",
                "answer": "5",
                "alternatives": [],
                "explanation": "(2+4+6+8)/4 = 20/4 = 5.",
            },
            {
                "question": "Hvad beskriver varians?",
                "answer": "spredning omkring middelværdien",
                "alternatives": ["hvor spredte data er"],
                "explanation": "Varians måler hvor meget observationerne afviger fra gennemsnittet.",
            },
            {
                "question": "Hvad er Q2 i et datasæt?",
                "answer": "medianen",
                "alternatives": ["median"],
                "explanation": "Q2 er den anden kvartil, altså medianen.",
            },
            {
                "question": "Kan spredning være negativ? (ja/nej)",
                "answer": "nej",
                "alternatives": [],
                "explanation": "Spredning er en kvadratrod og derfor ikke negativ.",
            },
        ],
        "Andengradspolynomier": [
            {
                "question": "Hvor mange nulpunkter har en andengradsfunktion hvis d=0?",
                "answer": "1",
                "alternatives": ["et", "ét"],
                "explanation": "Når diskriminanten er 0, er der ét dobbelt nulpunkt.",
            },
            {
                "question": "Hvad er toppunktets x-koordinat for f(x)=ax²+bx+c?",
                "answer": "-b/(2a)",
                "alternatives": ["-b/2a"],
                "explanation": "Formlen for toppunktets x-værdi er -b/(2a).",
            },
            {
                "question": "Har parablen f(x)=x²+2x+5 et maksimum eller minimum?",
                "answer": "minimum",
                "alternatives": [],
                "explanation": "Når a>0, vender parablen opad og har minimum.",
            },
            {
                "question": "Hvad er diskriminanten for f(x)=x²+2x+1?",
                "answer": "0",
                "alternatives": [],
                "explanation": "d = 2² - 4·1·1 = 4 - 4 = 0.",
            },
            {
                "question": "Hvad betyder det hvis d<0?",
                "answer": "ingen nulpunkter",
                "alternatives": ["grafen skærer ikke x-aksen"],
                "explanation": "Negativ diskriminant giver ingen reelle rødder.",
            },
        ],
    },
    "Matematik B": {
        "Differentialregning": [
            {
                "question": "Differentiér f(x)=x^4.",
                "answer": "4x^3",
                "alternatives": ["4*x^3"],
                "explanation": "Potensreglen giver 4x³.",
            },
            {
                "question": "Differentiér f(x)=e^x.",
                "answer": "e^x",
                "alternatives": [],
                "explanation": "Den afledte af e^x er e^x.",
            },
            {
                "question": "Hvad betyder det hvis f'(x)>0?",
                "answer": "funktionen er stigende",
                "alternatives": ["stigende"],
                "explanation": "Positiv afledt betyder stigende funktion.",
            },
            {
                "question": "Hvad er tangenthældningen når f'(2)=5?",
                "answer": "5",
                "alternatives": [],
                "explanation": "Den afledte er tangenthældningen.",
            },
            {
                "question": "Sætningen f'(x)=0 bruges typisk til at finde hvad?",
                "answer": "ekstrema",
                "alternatives": ["kritiske punkter", "top- og bundpunkter"],
                "explanation": "Når f'(x)=0, undersøger man om der er top- eller bundpunkt.",
            },
        ],
        "Lineær programmering": [
            {
                "question": "Hvilket område arbejder man i ved lineær programmering?",
                "answer": "det gyldige område",
                "alternatives": ["polygonområdet", "det tilladte område"],
                "explanation": "Løsningen findes i det område der opfylder alle bibetingelser.",
            },
            {
                "question": "Hvor skal målfunktionen testes?",
                "answer": "i hjørnepunkterne",
                "alternatives": ["hjørnepunkter"],
                "explanation": "Ved lineær programmering findes optimum i et hjørnepunkt.",
            },
            {
                "question": "Er x≥0 og y≥0 typisk en del af modellen? (ja/nej)",
                "answer": "ja",
                "alternatives": [],
                "explanation": "Ofte kræves ikke-negative variable.",
            },
            {
                "question": "Hvad kaldes linjer som Z=ax+by=t i planen?",
                "answer": "niveaulinjer",
                "alternatives": ["niveaukurver"],
                "explanation": "De viser samme værdi af målfunktionen.",
            },
            {
                "question": "Kan man bare 'se' det rigtige hjørnepunkt uden at regne? (ja/nej)",
                "answer": "nej",
                "alternatives": [],
                "explanation": "Alle relevante hjørnepunkter bør testes.",
            },
        ],
        "Sandsynlighedsregning": [
            {
                "question": "Hvad er sandsynligheden for plat ved ét kast med fair mønt?",
                "answer": "1/2",
                "alternatives": ["0.5", "0,5"],
                "explanation": "Der er 1 gunstigt udfald ud af 2 mulige.",
            },
            {
                "question": "Hvad står k for i P(X=k)=C(n,k)p^k(1-p)^(n-k)?",
                "answer": "antal succeser",
                "alternatives": ["succeser"],
                "explanation": "k er antallet af succeser.",
            },
            {
                "question": "Hvad er middelværdien for en binomialfordeling?",
                "answer": "n·p",
                "alternatives": ["np"],
                "explanation": "μ = n·p.",
            },
            {
                "question": "Hvad er variansen for en binomialfordeling?",
                "answer": "n·p·(1-p)",
                "alternatives": ["np(1-p)"],
                "explanation": "σ² = n·p·(1-p).",
            },
            {
                "question": "Hvornår bruges normalfordeling ofte som tilnærmelse?",
                "answer": "når n er stor",
                "alternatives": ["ved stor stikprøve", "når antallet af forsøg er stort"],
                "explanation": "Ved store n kan binomialfordelingen ofte tilnærmes med normalfordeling.",
            },
        ],
        "Konfidensinterval & hypotesetest": [
            {
                "question": "Hvad er nulhypotesen normalt skrevet som?",
                "answer": "h0",
                "alternatives": ["H0", "H₀"],
                "explanation": "Nulhypotesen betegnes H₀.",
            },
            {
                "question": "Hvad er alternativhypotesen normalt skrevet som?",
                "answer": "h1",
                "alternatives": ["H1", "H₁"],
                "explanation": "Alternativhypotesen betegnes H₁.",
            },
            {
                "question": "Hvis p-værdi er 0,12 ved 5% niveau, forkaster man så H₀? (ja/nej)",
                "answer": "nej",
                "alternatives": [],
                "explanation": "0,12 > 0,05, så H₀ forkastes ikke.",
            },
            {
                "question": "Et konfidensinterval for en andel bruger typisk hvilken hat-parameter?",
                "answer": "p̂",
                "alternatives": ["phat", "p-hat"],
                "explanation": "For andele bruges estimatet p̂.",
            },
            {
                "question": "Hvad er et signifikansniveau på 5% skrevet som decimaltal?",
                "answer": "0.05",
                "alternatives": ["0,05"],
                "explanation": "5% = 0,05.",
            },
        ],
    },
    "Matematik A": {
        "Integralregning": [
            {
                "question": "Bestem ∫ 5 dx.",
                "answer": "5x+c",
                "alternatives": ["5x + c", "5x+C", "5x+c"],
                "explanation": "Integral af en konstant a er a·x + C.",
            },
            {
                "question": "Bestem ∫ x² dx.",
                "answer": "x^3/3+c",
                "alternatives": ["x^3/3 + c", "x³/3+c", "x³/3 + c"],
                "explanation": "Potensreglen giver x³/3 + C.",
            },
            {
                "question": "Hvad er ∫₁³ 2x dx?",
                "answer": "8",
                "alternatives": [],
                "explanation": "Stamfunktion er x². F(3)-F(1)=9-1=8.",
            },
            {
                "question": "Hvad skal man huske ved ubestemte integraler?",
                "answer": "+c",
                "alternatives": ["c", "integrationskonstant"],
                "explanation": "Ubestemte integraler skal have integrationskonstanten med.",
            },
            {
                "question": "Hvad trækker man fra hvad ved areal mellem to grafer?",
                "answer": "øverste minus nederste",
                "alternatives": ["den øverste funktion minus den nederste"],
                "explanation": "Arealet findes som integral af øverste minus nederste funktion.",
            },
        ],
        "Differentialligninger": [
            {
                "question": "Hvad er den generelle løsning til y'=ky?",
                "answer": "c·e^(kx)",
                "alternatives": ["C·e^(kx)", "ce^(kx)", "Ce^(kx)"],
                "explanation": "Eksponentiel vækstmodel har løsning y=C·e^(kx).",
            },
            {
                "question": "Hvad bestemmer konstanten C normalt?",
                "answer": "begyndelsesværdien",
                "alternatives": ["initialbetingelsen", "startværdien"],
                "explanation": "C findes ved at indsætte den givne begyndelsesværdi.",
            },
            {
                "question": "Er logistisk vækst begrænset eller ubegrænset?",
                "answer": "begrænset",
                "alternatives": [],
                "explanation": "Logistisk vækst bremses af bærekapaciteten.",
            },
            {
                "question": "Hvad står M for i logistisk vækst?",
                "answer": "bærekapacitet",
                "alternatives": ["maksimal population", "maksimal størrelse"],
                "explanation": "M er den øvre grænse modellen nærmer sig.",
            },
            {
                "question": "Hvad betyder y'=ky i ord?",
                "answer": "vækstraten er proportional med størrelsen",
                "alternatives": ["ændringshastigheden er proportional med y"],
                "explanation": "Jo større y er, jo større er væksten.",
            },
        ],
        "Trigonometriske funktioner": [
            {
                "question": "Hvad er sin(π/2)?",
                "answer": "1",
                "alternatives": [],
                "explanation": "På enhedscirklen er sin(π/2)=1.",
            },
            {
                "question": "Hvad er cos(0)?",
                "answer": "1",
                "alternatives": [],
                "explanation": "På enhedscirklen er cos(0)=1.",
            },
            {
                "question": "Hvad er midterlinjen i f(x)=2sin(x)-3?",
                "answer": "-3",
                "alternatives": [],
                "explanation": "D-værdien er midterlinjen.",
            },
            {
                "question": "Hvad er amplituden i f(x)=-4sin(x)+1?",
                "answer": "4",
                "alternatives": [],
                "explanation": "Amplituden er |A|.",
            },
            {
                "question": "Hvad er perioden når B=4 i f(x)=A·sin(Bx+C)+D?",
                "answer": "pi/2",
                "alternatives": ["π/2"],
                "explanation": "T = 2π/4 = π/2.",
            },
        ],
        "Vektorer": [
            {
                "question": "Hvad er summen af (1,2) og (2,3)?",
                "answer": "(3,5)",
                "alternatives": ["3,5"],
                "explanation": "Man lægger koordinaterne sammen komponentvist.",
            },
            {
                "question": "Hvad er længden af vektoren (0,5)?",
                "answer": "5",
                "alternatives": [],
                "explanation": "√(0²+5²)=5.",
            },
            {
                "question": "Hvornår er to vektorer ortogonale?",
                "answer": "når prikproduktet er 0",
                "alternatives": ["når skalarproduktet er 0"],
                "explanation": "Prikprodukt 0 betyder vinkelrethed.",
            },
            {
                "question": "Hvad er prikproduktet af (2,0) og (3,4)?",
                "answer": "6",
                "alternatives": [],
                "explanation": "2·3 + 0·4 = 6.",
            },
            {
                "question": "Hvad bruges cos-formlen for vektorer typisk til?",
                "answer": "at finde vinklen mellem vektorer",
                "alternatives": ["finde vinklen"],
                "explanation": "Cosinus-formlen kobler prikprodukt og vinkel.",
            },
        ],
        "Keglesnit": [
            {
                "question": "Hvad er centrum i (x-3)² + (y+2)² = 25?",
                "answer": "(3,-2)",
                "alternatives": ["3,-2"],
                "explanation": "Standardformen er (x-h)² + (y-k)² = r².",
            },
            {
                "question": "Hvad er radius i (x+1)² + (y-4)² = 36?",
                "answer": "6",
                "alternatives": [],
                "explanation": "Radius er kvadratroden af 36.",
            },
            {
                "question": "Hvad er centrum i en ellipse på formen (x-h)²/a² + (y-k)²/b² = 1?",
                "answer": "(h,k)",
                "alternatives": [],
                "explanation": "Centrum aflæses direkte som (h,k).",
            },
            {
                "question": "Hvornår er en ellipse faktisk en cirkel?",
                "answer": "når a=b",
                "alternatives": ["a = b"],
                "explanation": "Lige store halvakser giver en cirkel.",
            },
            {
                "question": "Skal man ofte fuldende kvadratet for at omskrive til standardform? (ja/nej)",
                "answer": "ja",
                "alternatives": [],
                "explanation": "Det er en standardmetode ved keglesnit.",
            },
        ],
    },
}

MUNDTLIG_EKSAMEN_DATA = {
    "Matematik C": {
        "Lineære funktioner": {
            "prompt": "Præsentér lineære funktioner. Kom ind på forskrift, graf, hældning, skæring med y-aksen og hvordan man bestemmer forskriften ud fra to punkter.",
            "husk": [
                "Forklar først hvad en funktion er.",
                "Skriv forskriften f(x)=ax+b.",
                "Forklar betydningen af a og b.",
                "Vis hvordan a findes ud fra to punkter.",
                "Forklar nulpunkt og skæring med akserne.",
            ],
            "opfoelgning": [
                "Hvordan ser grafen ud når a er negativ?",
                "Hvordan finder man forskriften ud fra to punkter?",
                "Hvad betyder b konkret?",
            ],
            "gode_saetninger": [
                "En lineær funktion beskriver konstant vækst eller konstant fald.",
                "Hældningskoefficienten a fortæller hvor meget y ændrer sig, når x stiger med 1.",
                "Konstanten b er funktionsværdien når x er 0.",
            ],
        },
        "Eksponentielle funktioner": {
            "prompt": "Præsentér eksponentielle funktioner. Kom ind på forskrift, graf, relativ vækst, begyndelsesværdi, fremskrivningsfaktor og løsning af eksponentielle ligninger.",
            "husk": [
                "Skriv f(x)=b·a^x.",
                "Forklar b som begyndelsesværdi og a som fremskrivningsfaktor.",
                "Forklar forskellen på eksponentiel vækst og fald.",
                "Nævn at relativ tilvækst er konstant.",
                "Forklar hvorfor ln bruges til at isolere x.",
            ],
            "opfoelgning": [
                "Hvornår er der vækst, og hvornår er der fald?",
                "Hvordan tester man eksponentiel adfærd?",
                "Hvad er fordoblings- og halveringskonstant?",
            ],
            "gode_saetninger": [
                "En eksponentiel funktion vokser eller falder med den samme procent i hvert interval.",
                "Når a er større end 1, har vi vækst, og når 0<a<1, har vi fald.",
                "Logaritmer bruges til at isolere eksponenten i en eksponentiel ligning.",
            ],
        },
        "Rentesregning & annuiteter": {
            "prompt": "Præsentér rentes- og annuitetsregning. Kom ind på rente, startkapital, slutkapital, terminsantal, annuitetsopsparing og annuitetslån.",
            "husk": [
                "Forklar Kₙ=K₀(1+r)^n.",
                "Forklar alle symboler i formlen.",
                "Nævn at r skal være decimal.",
                "Forklar forskellen på opsparing og lån.",
                "Vis at annuiteter bygger på faste indbetalinger eller ydelser.",
            ],
            "opfoelgning": [
                "Hvordan finder man renten hvis man kender start- og slutkapital?",
                "Hvordan finder man n?",
                "Hvad er forskellen på annuitetsopsparing og annuitetslån?",
            ],
            "gode_saetninger": [
                "Rentesregning er en eksponentiel model, fordi kapitalen ændres med en fast procent pr. termin.",
                "Ved annuitetsregning arbejder man med faste betalinger over flere terminer.",
            ],
        },
        "Deskriptiv statistik": {
            "prompt": "Præsentér deskriptiv statistik. Kom ind på middelværdi, varians, spredning, kvartiler, fraktiler og forskellen mellem diskret og grupperet variabel.",
            "husk": [
                "Forklar hvad datasættet beskriver.",
                "Definér middelværdi, varians og spredning.",
                "Forklar median og kvartiler.",
                "Nævn relevante diagrammer.",
                "Forklar forskellen på diskrete og grupperede data.",
            ],
            "opfoelgning": [
                "Hvad fortæller spredningen?",
                "Hvad er forskellen på median og middelværdi?",
                "Hvornår bruger man boxplot?",
            ],
            "gode_saetninger": [
                "Middelværdien beskriver centrum i data.",
                "Spredningen beskriver hvor langt observationerne typisk ligger fra middelværdien.",
                "Kvartiler deler datasættet i fire lige store dele.",
            ],
        },
        "Andengradspolynomier": {
            "prompt": "Præsentér andengradspolynomier. Kom ind på forskrift, graf, diskriminant, nulpunkter og toppunkt.",
            "husk": [
                "Skriv f(x)=ax²+bx+c.",
                "Forklar hvordan grafen ser ud.",
                "Definér diskriminanten d=b²-4ac.",
                "Forklar sammenhængen mellem d og antal nulpunkter.",
                "Vis hvordan toppunktet findes.",
            ],
            "opfoelgning": [
                "Hvornår har parablen maksimum og hvornår minimum?",
                "Hvad betyder d=0?",
                "Hvordan finder man toppunktet?",
            ],
            "gode_saetninger": [
                "En andengradsfunktion har graf som en parabel.",
                "Diskriminanten afgør hvor mange nulpunkter parablen har.",
                "Toppunktet er funktionens ekstremum.",
            ],
        },
    },
    "Matematik B": {
        "Differentialregning": {
            "prompt": "Præsentér differentialregning og funktionsundersøgelse. Kom ind på differentialkvotient, afledt funktion, tangenthældning, monotoniforhold og ekstrema.",
            "husk": [
                "Forklar hvad ændringshastighed er.",
                "Forklar at den afledte er en grænseværdi.",
                "Nævn de vigtigste differentiationsregler.",
                "Forklar hvordan f'(x)=0 bruges til at finde ekstrema.",
                "Knyt fortegnet for f' til voksende og aftagende funktion.",
            ],
            "opfoelgning": [
                "Hvorfor er differentialkvotienten en grænseværdi?",
                "Hvad betyder f'(x)>0 og f'(x)<0?",
                "Hvordan finder man tangentligningen?",
            ],
            "gode_saetninger": [
                "Den afledte funktion beskriver ændringshastigheden.",
                "Differentialkvotienten giver hældningen på tangenten i et punkt.",
                "Fortegnet for den afledte afgør om funktionen er voksende eller aftagende.",
            ],
        },
        "Lineær programmering": {
            "prompt": "Præsentér lineær programmering. Kom ind på bibetingelser, polygonområde, målfunktion, niveaulinjer og hvorfor optimum findes i et hjørnepunkt.",
            "husk": [
                "Forklar hvad variablene betyder.",
                "Opskriv bibetingelser som uligheder.",
                "Forklar det gyldige område.",
                "Forklar målfunktionen Z=ax+by.",
                "Forklar hvorfor hjørnepunkter testes.",
            ],
            "opfoelgning": [
                "Hvad er en niveaulinje?",
                "Hvordan finder man hjørnepunkterne?",
                "Hvorfor ligger optimum i et hjørnepunkt?",
            ],
            "gode_saetninger": [
                "Lineær programmering bruges til at optimere under lineære begrænsninger.",
                "Løsningen findes i det gyldige område og testes i hjørnepunkterne.",
                "Niveaulinjer har samme hældning for samme målfunktion.",
            ],
        },
        "Sandsynlighedsregning": {
            "prompt": "Præsentér sandsynlighedsregning. Kom ind på udfald, hændelser, komplementære hændelser, uafhængighed, binomialfordeling og normalfordeling.",
            "husk": [
                "Forklar hvad et sandsynlighedsfelt er.",
                "Definér hændelse og udfald.",
                "Forklar komplementære og disjunkte hændelser.",
                "Nævn forudsætninger for binomialfordeling.",
                "Forklar kort hvornår normalfordeling bruges.",
            ],
            "opfoelgning": [
                "Hvad betyder uafhængige hændelser?",
                "Hvad er middelværdi og varians i binomialfordelingen?",
                "Hvornår kan man bruge normaltilnærmelse?",
            ],
            "gode_saetninger": [
                "Sandsynlighed er et mål for hvor sandsynligt et udfald er.",
                "Binomialfordelingen bruges ved n uafhængige forsøg med to mulige udfald.",
                "Normalfordelingen anvendes ofte til kontinuerte data eller som tilnærmelse.",
            ],
        },
        "Konfidensinterval & hypotesetest": {
            "prompt": "Præsentér konfidensintervaller og hypotesetest. Kom ind på population, stikprøve, estimater, nulhypotese, alternativ hypotese, p-værdi og signifikansniveau.",
            "husk": [
                "Forklar forskellen på population og stikprøve.",
                "Definér punktestimat og intervalestimat.",
                "Forklar H₀ og H₁.",
                "Forklar hvad p-værdien betyder.",
                "Nævn hvordan man træffer beslutning ved 5% niveau.",
            ],
            "opfoelgning": [
                "Hvad betyder et 95%-konfidensinterval?",
                "Hvornår forkaster man H₀?",
                "Hvad er forskellen på estimering og test?",
            ],
            "gode_saetninger": [
                "Et konfidensinterval angiver et sandsynligt interval for en ukendt parameter.",
                "En hypotesetest undersøger om data er forenelige med nulhypotesen.",
                "Når p-værdien er mindre end signifikansniveauet, forkastes H₀.",
            ],
        },
    },
    "Matematik A": {
        "Integralregning": {
            "prompt": "Præsentér integralregning. Kom ind på ubestemte og bestemte integraler, stamfunktioner, hovedsætningen og sammenhængen mellem integral og areal.",
            "husk": [
                "Forklar forskellen på ubestemt og bestemt integral.",
                "Definér stamfunktion.",
                "Nævn de vigtigste integrationsregler.",
                "Forklar F(b)-F(a).",
                "Forklar areal under kurven og areal mellem grafer.",
            ],
            "opfoelgning": [
                "Hvad siger integralregningens hovedsætning?",
                "Hvorfor er +C kun med ved ubestemte integraler?",
                "Hvordan håndterer man areal mellem to grafer?",
            ],
            "gode_saetninger": [
                "Integralregning er den omvendte proces af differentialregning.",
                "Et ubestemt integral giver en stamfunktion, mens et bestemt integral giver et tal.",
                "Det bestemte integral beregnes som F(b)-F(a).",
            ],
        },
        "Differentialligninger": {
            "prompt": "Præsentér differentialligninger. Kom ind på eksponentiel vækst, logistisk vækst, separable differentialligninger og hvordan begyndelsesbetingelser bestemmer løsningen.",
            "husk": [
                "Forklar hvad en differentialligning er.",
                "Forklar modellen y'=ky og dens løsning.",
                "Forklar logistisk vækst og bærekapacitet.",
                "Nævn betydningen af begyndelsesværdi.",
                "Forklar hvad det vil sige at eftervise en løsning.",
            ],
            "opfoelgning": [
                "Hvad er forskellen på eksponentiel og logistisk vækst?",
                "Hvordan bestemmes konstanten C?",
                "Hvad betyder bærekapacitet?",
            ],
            "gode_saetninger": [
                "En differentialligning forbinder en funktion med dens afledte.",
                "Ved eksponentiel vækst er ændringshastigheden proportional med størrelsen.",
                "Logistisk vækst har en indbygget bremsefaktor og nærmer sig en øvre grænse.",
            ],
        },
        "Trigonometriske funktioner": {
            "prompt": "Præsentér trigonometriske funktioner. Kom ind på enhedscirklen, radianer, graferne for sinus og cosinus og parametrene i harmonisk svingning.",
            "husk": [
                "Forklar enhedscirklen.",
                "Forklar sammenhængen mellem enhedscirklen og graferne.",
                "Forklar radianmål.",
                "Gennemgå parametrene a, b, c og d i a·sin(bx+c)+d.",
                "Forklar amplitude, periode, faseforskydning og midterlinje.",
            ],
            "opfoelgning": [
                "Hvordan fremkommer sinusgrafen fra enhedscirklen?",
                "Hvad betyder b for perioden?",
                "Hvad betyder c og d?",
            ],
            "gode_saetninger": [
                "De trigonometriske funktioner beskriver svingninger og periodiske fænomener.",
                "På enhedscirklen er cosinus x-koordinaten og sinus y-koordinaten.",
                "I en harmonisk svingning bestemmer a amplituden og b perioden.",
            ],
        },
        "Vektorer": {
            "prompt": "Præsentér vektorer. Kom ind på koordinater, længde, addition, skalarprodukt, projektion og vinkel mellem vektorer.",
            "husk": [
                "Forklar hvad en vektor er.",
                "Vis hvordan koordinater aflæses.",
                "Forklar længdeformlen.",
                "Forklar skalarproduktet.",
                "Nævn ortogonalitet og vinkelberegning.",
            ],
            "opfoelgning": [
                "Hvordan findes koordinaterne til AB-vektoren?",
                "Hvornår er to vektorer ortogonale?",
                "Hvad bruges skalarproduktet til?",
            ],
            "gode_saetninger": [
                "En vektor har både retning og længde.",
                "Skalarproduktet kombinerer to vektorer til et tal.",
                "Hvis skalarproduktet er 0, er vektorerne vinkelrette.",
            ],
        },
        "Keglesnit": {
            "prompt": "Præsentér keglesnit. Kom ind på cirkel og ellipse, standardformer, centrum, radius/halvakser og omskrivning til standardform.",
            "husk": [
                "Forklar hvad keglesnit er.",
                "Skriv standardformen for en cirkel.",
                "Skriv standardformen for en ellipse.",
                "Forklar hvordan centrum aflæses.",
                "Nævn at fuldendelse af kvadrat ofte bruges ved omskrivning.",
            ],
            "opfoelgning": [
                "Hvornår er en ellipse en cirkel?",
                "Hvordan finder man radius i standardformen?",
                "Hvordan omskriver man en andengradsligning til cirkelform?",
            ],
            "gode_saetninger": [
                "Keglesnit er kurver der opstår ved at skære en kegle med et plan.",
                "En cirkel er et specialtilfælde af en ellipse.",
                "Ved omskrivning til standardform bruger man ofte fuldendelse af kvadrat.",
            ],
        },
    },
}
# =========================================================
# HELPERS
# =========================================================
def normalize_text(text: str) -> str:
    return (
        str(text)
        .strip()
        .lower()
        .replace(" ", "")
        .replace("·", "")
        .replace("*", "")
        .replace("₀", "0")
        .replace("²", "^2")
        .replace("π", "pi")
    )


def check_answer(user_answer: str, correct_answer: str, alternatives: list) -> bool:
    user_answer = normalize_text(user_answer)
    correct_answer = normalize_text(correct_answer)
    alternatives = [normalize_text(ans) for ans in alternatives]

    return user_answer == correct_answer or user_answer in alternatives

def reset_quiz():
    keys = [
        "quiz_started",
        "quiz_level",
        "quiz_topic",
        "quiz_questions",
        "quiz_index",
        "quiz_score",
        "quiz_feedback",
        "quiz_answered",
    ]
    for key in keys:
        if key in st.session_state:
            del st.session_state[key]


def start_quiz(level: str, topic: str):
    questions = MATH_DATA[level][topic]["quiz"].copy()
    random.shuffle(questions)
    st.session_state.quiz_started = True
    st.session_state.quiz_level = level
    st.session_state.quiz_topic = topic
    st.session_state.quiz_questions = questions
    st.session_state.quiz_index = 0
    st.session_state.quiz_score = 0
    st.session_state.quiz_feedback = None
    st.session_state.quiz_answered = False

def render_card(title: str, content: str):
    st.markdown(
        f"""
        <div class="card">
            <h3>{title}</h3>
            <div class="muted">{content}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
def extend_quiz_bank():
    for level, topics in EXTRA_QUIZ_QUESTIONS.items():
        for topic, questions in topics.items():
            if level in MATH_DATA and topic in MATH_DATA[level]:
                MATH_DATA[level][topic]["quiz"].extend(questions)


extend_quiz_bank()
# =========================================================
# MINI EXAM HELPERS
# =========================================================
def build_mini_exam(level: str, num_tasks: int = 4):
    tasks = []
    for topic, task_data in EXAM_TASKS[level].items():
        tasks.append(
            {
                "topic": topic,
                "opgave": task_data["opgave"],
                "løsningsforslag": task_data["løsningsforslag"],
            }
        )

    random.shuffle(tasks)
    return tasks[: min(num_tasks, len(tasks))]


def start_mini_exam(level: str, num_tasks: int):
    st.session_state.mini_exam_started = True
    st.session_state.mini_exam_level = level
    st.session_state.mini_exam_tasks = build_mini_exam(level, num_tasks)

def extend_quiz_bank():
    for level, topics in EXTRA_QUIZ_QUESTIONS.items():
        for topic, questions in topics.items():
            if level in MATH_DATA and topic in MATH_DATA[level]:
                MATH_DATA[level][topic]["quiz"].extend(questions)


extend_quiz_bank()

# =========================================================
# SIDEBAR
# =========================================================
page = st.sidebar.radio(
    "Vælg side",
    [
        "Forside",
        "Om appen",
        "Emneoversigt",
        "Quiz",
        "Eksamensopgaver",
        "Mini-eksamen",
        "Mundtlig eksamen",
        "Hurtig repetition",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Vælg et niveau og et emne, læs forklaringerne, og test dig selv i quizzen."
)

# =========================================================
# FORSIDE
# =========================================================
if page == "Forside":
    st.markdown(
        """
        <div class="hero">
            <h1>Læs op til Matematik A med mig</h1>
            <p>
                En flot og enkel læringsapp til Matematik C, B og A.
                Brug den til repetition, mundtlig træning, formler,
                klassiske fejl og små quizzer før eksamen.
            </p>
            <div class="pill-row">
                <div class="pill">Matematik C</div>
                <div class="pill">Matematik B</div>
                <div class="pill">Matematik A</div>
                <div class="pill">Quiz & repetition</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.markdown(
            """
            <div class="card">
                <div class="small-badge">Kom i gang</div>
                <h3>Emneoversigt</h3>
                <div class="muted">
                    Vælg niveau og emne, og få et klart overblik over
                    hvad emnet handler om, formler, metode og typiske fejl.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <div class="small-badge">Øv dig</div>
                <h3>Quiz</h3>
                <div class="muted">
                    Tag små quizzer inden for hvert emne og få direkte feedback
                    på dine svar.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div class="card">
            <div class="small-badge">Eksamensniveau</div>
            <h3>Eksamensopgaver</h3>
            <div class="muted">
                Træn rigtige eksamensopgaver med løsningsforslag.
            </div>
        </div>
        """,
            unsafe_allow_html=True,
    )
    with col4:
        st.markdown(
         """
        <div class="card">
            <div class="small-badge">Test dig selv</div>
            <h3>Mini-eksamen</h3>
            <div class="muted">
                Få en blanding af opgaver og træn som til en rigtig eksamen.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with col5:
        st.markdown(
        """
            <div class="card">
                <div class="small-badge">Mundtlig træning</div>
                <h3>Mundtlig eksamen</h3>
                <div class="muted">
                Øv hvordan du forklarer emnerne højt og forbered dig på opfølgende spørgsmål.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with col6:
        st.markdown(
        """
            <div class="card">
                <div class="small-badge">Husk det vigtigste</div>
                <h3>Hurtig repetition</h3>
                <div class="muted">
                    Få et kort overblik over de vigtigste regler og begreber
                    lige før øvning eller eksamen.
                </div>
            </div>
            """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">Sådan bruger du appen</div>', unsafe_allow_html=True)

    st.markdown(
    """
    <div class="card">
        <h3>Anbefalet rækkefølge til eksamensoplæsning</h3>
        <div class="muted">
            <p><b>1.</b> Start i <b>Emneoversigt</b> og få et overblik over alle emner.</p>
            <p><b>2.</b> Brug <b>Quiz</b> til at teste din forståelse og sikre, at du kan de vigtigste begreber og formler.</p>
            <p><b>3.</b> Arbejd med <b>Eksamensopgaver</b> — find papir eller computer frem og løs opgaverne som til en rigtig eksamen.</p>
            <p><b>4.</b> Tag en <b>Mini-eksamen</b>, hvor du bliver testet i flere emner på én gang — præcis som til eksamen.</p>
            <p><b>5.</b> Når den skriftlige del sidder, kan du bruge <b>Mundtlig eksamen</b> til at øve forklaringer, eksempler og faglig formidling.</p>
            <p><b>6.</b> Brug <b>Hurtig repetition</b>, når du er på farten eller lige skal genopfriske det vigtigste.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# EMNEOVERSIGT
# =========================================================
elif page == "Emneoversigt":
    st.markdown('<div class="section-title">Emneoversigt</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        level = st.selectbox("Vælg niveau", list(MATH_DATA.keys()))

    with col2:
        topic = st.selectbox("Vælg emne", list(MATH_DATA[level].keys()))

    content = MATH_DATA[level][topic]

    st.markdown(
        f"""
        <div class="card">
            <div class="small-badge">{level}</div>
            <h3>{topic}</h3>
            <div class="muted">
                Her kan du læse emnet igennem trin for trin og forberede dig til både skriftlig og mundtlig matematik.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Hvad er det?", "Formler", "Trin-for-trin", "Mundtlig hjælp", "Klassiske fejl"]
    )

    with tab1:
        render_card("Hvad er det?", content["hvad_er_det"])

    with tab2:
        formulas_html = "<br>".join([f"• {formula}" for formula in content["formler"]])
        render_card("Formler", formulas_html)

    with tab3:
        steps_html = "<br>".join(
            [f"{i}. {step}" for i, step in enumerate(content["trin"], start=1)]
        )
        render_card("Trin-for-trin", steps_html)

    with tab4:
        render_card("Mundtlig hjælp", content["mundtlig"])

    with tab5:
        mistakes_html = "<br>".join([f"• {mistake}" for mistake in content["fejl"]])
        render_card("Klassiske fejl", mistakes_html)


    st.markdown("### Klar til at teste dig selv?")
    if st.button("Start quiz i dette emne"):
        start_quiz(level, topic)
        st.success("Quizzen er startet. Gå til siden 'Quiz' i menuen til venstre.")

# =========================================================
# QUIZ
# =========================================================
elif page == "Quiz":
    st.markdown('<div class="section-title">Quiz</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        selected_level = st.selectbox("Vælg niveau til quiz", list(MATH_DATA.keys()), key="quiz_level_select")
    with col2:
        selected_topic = st.selectbox(
            "Vælg emne til quiz",
            list(MATH_DATA[selected_level].keys()),
            key="quiz_topic_select",
        )

    button_col1, button_col2 = st.columns(2)

    with button_col1:
        if st.button("Start / genstart quiz"):
            start_quiz(selected_level, selected_topic)

    with button_col2:
        if st.button("Nulstil quiz"):
            reset_quiz()
            st.rerun()

    if not st.session_state.get("quiz_started", False):
        st.markdown(
            """
            <div class="card">
                <h3>Ingen quiz startet endnu</h3>
                <div class="muted">
                    Vælg niveau og emne ovenfor, og tryk derefter på
                    <b>Start / genstart quiz</b>.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        questions = st.session_state.quiz_questions
        idx = st.session_state.quiz_index

        st.markdown(
            f"""
            <div class="card">
                <div class="small-badge">{st.session_state.quiz_level}</div>
                <h3>{st.session_state.quiz_topic}</h3>
                <div class="muted">
                    Spørgsmål {min(idx + 1, len(questions))} ud af {len(questions)}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if idx < len(questions):
            q = questions[idx]

            st.markdown(
                f"""
                <div class="card">
                    <h3>{q["question"]}</h3>
                </div>
                """,
                unsafe_allow_html=True,
            )

            answer_key = f"user_answer_{idx}"
            user_answer = st.text_input("Skriv dit svar her", key=answer_key)

            if not st.session_state.quiz_answered:
                if st.button("Tjek svar"):
                    is_correct = check_answer(
                        user_answer=user_answer,
                        correct_answer=q["answer"],
                        alternatives=q["alternatives"],
                    )

                    if is_correct:
                        st.session_state.quiz_score += 1
                        st.session_state.quiz_feedback = {
                            "type": "success",
                            "message": f"✅ Korrekt!\n\nForklaring: {q['explanation']}",
                        }
                    else:
                        st.session_state.quiz_feedback = {
                            "type": "error",
                            "message": (
                                f"❌ Ikke helt rigtigt.\n\n"
                                f"Rigtigt svar: {q['answer']}\n\n"
                                f"Forklaring: {q['explanation']}"
                            ),
                        }

                    st.session_state.quiz_answered = True
                    st.rerun()

            if st.session_state.quiz_feedback:
                feedback = st.session_state.quiz_feedback
                if feedback["type"] == "success":
                    st.success(feedback["message"])
                else:
                    st.error(feedback["message"])

            if st.session_state.quiz_answered:
                if st.button("Næste spørgsmål"):
                    st.session_state.quiz_index += 1
                    st.session_state.quiz_feedback = None
                    st.session_state.quiz_answered = False
                    st.rerun()

        else:
            score = st.session_state.quiz_score
            total = len(questions)
            percentage = round((score / total) * 100) if total > 0 else 0

            st.markdown(
                f"""
                <div class="score-box">
                    Quiz færdig! Du fik {score} ud af {total} rigtige ({percentage}%).
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.write("")

            if percentage == 100:
                st.success("Perfekt — det emne sidder virkelig godt fast.")
                st.balloons()
            elif percentage >= 70:
                st.success("Rigtig flot. Du er godt på vej.")
            elif percentage >= 50:
                st.warning("Godt arbejde. Tag gerne quizzen igen for at blive endnu mere sikker.")
            else:
                st.info("Læs emnet igennem igen i Emneoversigt og prøv quizzen én gang til.")

# =========================================================
# MINI-EKSAMEN
# =========================================================
elif page == "Mini-eksamen":
    st.markdown('<div class="section-title">Mini-eksamen</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        mini_exam_level = st.selectbox(
            "Vælg niveau",
            list(EXAM_TASKS.keys()),
            key="mini_exam_level_select"
        )
    with col2:
        mini_exam_count = st.selectbox(
            "Antal opgaver",
            [3, 4, 5],
            index=1,
            key="mini_exam_count_select"
        )

    st.markdown(
        """
        <div class="card">
            <h3>Træn som til eksamen</h3>
            <div class="muted">
                Her får du en blanding af opgaver fra det valgte niveau.
                Prøv at løse dem selv først, og se derefter løsningsforslagene.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_a, col_b = st.columns(2)

    with col_a:
        if st.button("Start mini-eksamen"):
            start_mini_exam(mini_exam_level, mini_exam_count)
            st.rerun()

    with col_b:
        if st.button("Nulstil mini-eksamen"):
            for key in ["mini_exam_started", "mini_exam_level", "mini_exam_tasks"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

    if not st.session_state.get("mini_exam_started", False):
        st.info("Vælg niveau og antal opgaver, og tryk på 'Start mini-eksamen'.")
    else:
        st.markdown(
            f"""
            <div class="card">
                <div class="small-badge">{st.session_state["mini_exam_level"]}</div>
                <h3>Din mini-eksamen</h3>
                <div class="muted">
                    Du har fået {len(st.session_state["mini_exam_tasks"])} opgaver.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        for i, task in enumerate(st.session_state["mini_exam_tasks"], start=1):
            st.markdown(
                f"""
                <div class="card">
                    <div class="small-badge">Opgave {i}</div>
                    <h3>{task["topic"]}</h3>
                    <div class="muted" style="white-space: pre-line;">{task["opgave"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            show_key = f"show_solution_mini_{i}"
            show_solution = st.checkbox(
                f"Vis løsningsforslag til opgave {i}",
                key=show_key
            )

            if show_solution:
                st.markdown(
                    f"""
                    <div class="card">
                        <h3>Løsningsforslag</h3>
                        <div class="muted" style="white-space: pre-line;">{task["løsningsforslag"]}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

# =========================================================
# MUNDTLIG EKSAMEN
# =========================================================
elif page == "Mundtlig eksamen":
    st.markdown('<div class="section-title">Mundtlig eksamen</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        oral_level = st.selectbox("Vælg niveau", list(MUNDTLIG_EKSAMEN_DATA.keys()), key="oral_level")
    with col2:
        oral_topic = st.selectbox("Vælg emne", list(MUNDTLIG_EKSAMEN_DATA[oral_level].keys()), key="oral_topic")

    oral = MUNDTLIG_EKSAMEN_DATA[oral_level][oral_topic]

    st.markdown(
        f"""
        <div class="card">
            <div class="small-badge">{oral_level}</div>
            <h3>{oral_topic}</h3>
            <div class="muted">
                Brug denne side til at øve det, du skal sige højt til den mundtlige eksamen.
                Skriv stikord først, forklar derefter emnet højt, og sammenlign til sidst med strukturen nedenfor.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Mundtligt eksamensspørgsmål")
    st.markdown(
        f"""
        <div class="card">
            <div class="muted" style="white-space: pre-line;">{oral["prompt"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.text_area(
        "Skriv dine egne stikord / din egen forklaring her",
        height=180,
        key=f"oral_notes_{oral_level}_{oral_topic}",
        placeholder="Skriv fx definition, vigtigste formler, et eksempel, og hvordan du vil forklare det højt..."
    )

    st.checkbox("Jeg har forklaret emnet højt for mig selv", key=f"oral_spoken_{oral_level}_{oral_topic}")

    with st.expander("Hvad du bør komme ind på"):
        for item in oral["husk"]:
            st.markdown(f"- {item}")

    with st.expander("Mulige opfølgende spørgsmål fra lærer/censor"):
        for item in oral["opfoelgning"]:
            st.markdown(f"- {item}")

    with st.expander("Gode sætninger du kan bruge"):
        for item in oral["gode_saetninger"]:
            st.markdown(f"- {item}")

    st.markdown("### Hurtig mundtlig træning")
    st.markdown(
        """
        <div class="card">
            <div class="muted">
                1. Læs spørgsmålet højt<br>
                2. Tal i 2-4 minutter uden at kigge for meget ned<br>
                3. Brug dine stikord som støtte<br>
                4. Sammenlign bagefter med punkterne ovenfor<br>
                5. Prøv igen og gør forklaringen mere rolig og præcis
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
# =========================================================
# HURTIG REPETITION
# =========================================================
elif page == "Hurtig repetition":
    st.markdown('<div class="section-title">Hurtig repetition</div>', unsafe_allow_html=True)

    level = st.selectbox("Vælg niveau", list(QUICK_REVIEW.keys()), key="quick_review_level")

    st.markdown(
        f"""
        <div class="card">
            <div class="small-badge">{level}</div>
            <h3>Det vigtigste at huske</h3>
            <div class="muted">
                Brug denne side lige før eksamen eller når du vil have et hurtigt overblik.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for item in QUICK_REVIEW[level]:
        st.markdown(
            f"""
            <div class="review-item">
                {item}
            </div>
            """,
            unsafe_allow_html=True,
        )

# =========================================================
# EKSAMENSOPGAVER
# =========================================================
elif page == "Eksamensopgaver":
    st.markdown('<div class="section-title">Eksamensopgaver</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        exam_level = st.selectbox("Vælg niveau", list(EXAM_TASKS.keys()), key="exam_level")
    with col2:
        exam_topic = st.selectbox("Vælg emne", list(EXAM_TASKS[exam_level].keys()), key="exam_topic")

    selected_task = EXAM_TASKS[exam_level][exam_topic]

    st.markdown(
        f"""
        <div class="card">
            <div class="small-badge">{exam_level}</div>
            <h3>{exam_topic}</h3>
            <div class="muted">
                Brug opgaven som eksamenstræning. Prøv at løse den selv først, før du ser løsningsforslaget.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Opgave")
    st.markdown(
        f"""
        <div class="card">
            <div class="muted" style="white-space: pre-line;">{selected_task["opgave"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    show_solution = st.checkbox("Vis løsningsforslag")

    if show_solution:
        st.markdown("### Løsningsforslag")
        st.markdown(
            f"""
            <div class="card">
                <div class="muted" style="white-space: pre-line;">{selected_task["løsningsforslag"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# =========================================================
# OM APPEN
# =========================================================
elif page == "Om appen":
    st.markdown('<div class="section-title">Om appen</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">
            <h3>Læs op til Matematik A med mig</h3>
            <div class="muted">
                Denne app er lavet som en enkel og pæn læringsapp til Matematik C, B og A.
                Den er bygget i Streamlit og kan bruges til repetition, træning og eksamensforberedelse.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card">
            <h3>Det kan du bruge den til</h3>
            <div class="muted">
                • læse emner igennem på en overskuelig måde<br>
                • øve mundtlige forklaringer<br>
                • huske formler og metoder<br>
                • se klassiske fejl<br>
                • tage quizzer emne for emne
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card">
            <h3>Teknik</h3>
            <div class="muted">
                Appen bruger ikke AI eller eksterne API'er. Det gør den nem at deploye og nem at vedligeholde.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; color:#64748b; font-size:0.92rem; padding: 0.5rem 0 1.2rem 0;">
        Bygget af <b>Emina Gracanin</b> · Prototype til eksamensforberedelse i Matematik A
    </div>
    """,
    unsafe_allow_html=True,
)