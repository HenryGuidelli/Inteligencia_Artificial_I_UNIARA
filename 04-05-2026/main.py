import requests
import xml.etree.ElementTree as ET
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# =====================================================================
# 1. DADOS DE TREINAMENTO (Sua base local)
# =====================================================================
documentos_treinamento = [
    "sereno cooperação grande envolvente encorajador atencioso",
    "estupendo atencioso maravilhoso respeito apreciado entusiasmo motivador",
    "solidário encantador aplaudido estupendo hilariante bondoso aplaudível",
    "estima amizade incomparável fascinante",
    "espetacular aplaudível honroso",
    "glorioso admirável solidariedade satisfatório fabuloso",
    "adorável gentil consideração colaboração gratificante amizade",
    "sereno harmonioso entusiasmo estupendo glorioso solidariedade empolgante",
    "compreensão sublime excelente consideração cooperação celestial",
    "triunfante solidário empolgante sensacional estima",
    "perfeito fascinante aplaudido radiante aplaudível consideração vibrante",
    "companheirismo bondoso honroso",
    "celestial atencioso triunfo radioso apreciado glorioso sensacional tranquilo",
    "alegre pacífico compreensivo compaixão fascinante gratificante edificante confiante",
    "magnífico apaixonante estupendo gratificante honroso apoio generoso aplaudido",
    "sensacional divertido radioso resiliente grande respeitável",
    "adorável arrebatador altruísta gratidão união companheirismo",
    "estimulante cativante amável apetitoso estima apoio triunfo excepcional",
    "edificante amável amizade entusiasmo exultante fascinante compreensivo",
    "glorioso amável motivador",
    "perseverante envolvente empolgante altruísta respeito cooperação gratidão",
    "estupendo extraordinário perseverante união delicioso triunfo aplaudível",
    "celestial fascinante entusiasmo solidariedade prestigioso compaixão encorajamento",
    "conciliador divertido fantástico maravilhoso atencioso encorajamento cativante",
    "consideração aplaudível encorajador bom notável revigorante colaboração",
    "inspirador compreensão solidário revigorante",
    "radioso maravilha excelente cativante",
    "amável espetacular pacificador reconfortante encorajamento",
    "encorajador compreensivo companheirismo consolador fantástico cooperação",
    "apoio respeito amável excepcional generoso",
    "bom excelente satisfatório apoio maravilhoso magnífico respeitável",
    "solidariedade empolgante perfeito extraordinário envolvente",
    "encantador empolgante prestigioso",
    "entusiasmo empolgante solidário",
    "satisfatório carinhoso sereno estupendo estimulante aplaudido radioso ótimo",
    "aplaudível generoso extraordinário atencioso união",
    "compassivo respeito tranquilo apreciado união gratificante",
    "satisfatório seguro respeito",
    "triunfante prestigioso honroso compaixão",
    "fascinante união notável estimulante grande encantador encorajador motivador",
    "perfeito glorioso resiliente calmo exultante estimulante",
    "edificante aplaudido resiliente hilariante",
    "arrebatador cooperação admirável honroso radiante",
    "apreciado perseverante amável bom",
    "companheirismo apoio reconfortante",
    "respeito reconhecimento aplaudível consolador atencioso estimulante adorável triunfo",
    "celestial amável encantador",
    "carinhoso sublime espetacular entusiasmo",
    "amoroso alegre respeito amizade otimista",
    "amizade estimulante esplêndido companheirismo arrebatador",
    "reconfortante arrebatador compreensivo otimista admirável companheirismo",
    "consolador excepcional compassivo sublime otimista",
    "radiante bom triunfante",
    "amoroso compaixão paciente encorajamento",
    "entusiasta triunfo maravilha admirável apoio fenomenal arrebatador",
    "sensacional júbilo encantador",
    "envolvente excepcional arrebatador",
    "otimista entusiasta amoroso magnífico estima encorajamento",
    "solidário energizante fenomenal fabuloso grande compreensão",
    "divertido fantástico solidariedade radiante",
    "generoso solidariedade consideração solidário compassivo",
    "empolgante espetacular reconfortante consideração",
    "seguro confiante pacífico glorioso excepcional fenomenal vibrante revigorante",
    "otimista alegre satisfatório exultante excelente inspirador cooperação",
    "perfeito apreciado radioso extraordinário ótimo envolvente tolerante excepcional",
    "altruísta seguro satisfatório consolador notável encorajador compreensão gentil",
    "fascinante pacificador encorajador união triunfante respeitável tranquilo honroso",
    "união inspirador radiante notável",
    "otimista apetitoso extraordinário pacificador perseverante gentil compreensão maravilhoso",
    "estupendo reconfortante prestigioso bom honroso",
    "compreensivo alegre empolgante maravilha envolvente respeito radiante inspirador",
    "gentil compaixão consideração",
    "triunfante prestigioso sereno saboroso admirável energizante",
    "amizade tranquilo edificante incomparável",
    "compassivo gentil fabuloso união entusiasta",
    "maravilha júbilo conciliador solidário respeitável",
    "amizade entusiasta exultante",
    "gratificante pacificador tolerante respeitável otimista resiliente incomparável",
    "encorajamento entusiasmo consolador apaixonante amável radioso gratificante maravilha",
    "excepcional paciente energizante aplaudível",
    "amoroso sublime sensacional glorioso bondoso tranquilo prestigioso",
    "encorajamento calmo estima amizade fabuloso colaboração generoso compassivo",
    "generoso fenomenal maravilha triunfante",
    "solidariedade aplaudível compassivo entusiasmo excelente excepcional",
    "esplêndido celestial otimista sereno incrível amável calmo",
    "empolgante apreciado motivador",
    "celestial ótimo resiliente cativante entusiasmo",
    "notável entusiasta exultante celestial delicioso",
    "bom pacificador admirável grande apaixonante",
    "fenomenal conciliador honroso compaixão",
    "otimista fascinante alegre hilariante amoroso grande",
    "hilariante alegre otimista cativante altruísta perfeito",
    "maravilhoso adorável amizade grande cooperação estima triunfo harmonioso",
    "afetuoso bondoso estima apaixonante envolvente excepcional radioso",
    "união grande vibrante aplaudido encorajamento prestigioso",
    "prestigioso perfeito cativante",
    "perseverante otimista incrível união satisfatório",
    "tranquilo fabuloso união paciente encantador",
    "compaixão pacificador energizante",
    "sensacional sublime sereno satisfatório",
    "eu amo",
    "mísero melancólico desagradável desalentador desfavorável",
    "desesperador desesperador abafado",
    "vexante abatido aborrecido",
    "inaceitável melancólico deprimente",
    "aborrecido isolado doloroso",
    "miserável desconsolado péssimo repelente desapontante aterrorizante desalentador ruim",
    "deprimido repugnante horrendo assustador inaceitável vexante",
    "solitário desalentador deprimido decepcionante assustador",
    "abatido nefasto aborrecido repugnante desinteressante inaceitável desesperador asqueroso",
    "inaceitável abatido desastroso mal-humorado desastroso",
    "irritante opressivo odioso",
    "inaceitável aterrorizante desesperador desanimador",
    "desgraçado nefasto repugnante asqueroso desagradável",
    "terrível odioso desastroso cínico",
    "pavoroso mísero odioso incomodativo triste assombroso desalentador infeliz",
    "irritante assombroso doloroso desesperador opressivo desastroso desconfortável",
    "pavoroso terrífico repelente deprimido derrotista desanimador horrível aborrecido",
    "desalentador enfadonho abafado derrotista inaceitável asqueroso",
    "desconsolado vexante inaceitável solitário",
    "cínico insuportável embaraçoso nojento lamentável vexatório",
    "vexante entediante desastroso desagradável inaceitável abafado desesperador desalentador",
    "desagradável desmoralizante vexatório embaraçoso desesperador",
    "desagradável desalentador desesperado aterrorizante medonho",
    "desapontante embaraçoso desmoralizante inaceitável indesejável melancólico abominável",
    "enfadonho deprimido triste",
    "desesperado entediante derrotista inaceitável doloroso frustrante solitário",
    "abatido desmoralizante entristecido aborrecido",
    "mísero desfavorável embaraçoso desalentador horrível entristecido detestável",
    "mal-humorado apavorante ruim decepcionante",
    "assustador horrendo embaraçoso entristecido terrível",
    "desalentador desgraçado horrível desagradável apavorante desconfortável chato",
    "vergonhoso abominável pavoroso vexante desfavorável deprimido",
    "aborrecido medonho assustador entediante insatisfatório",
    "inaceitável repelente aborrecido deprimente desastroso aborrecido entristecido desanimador",
    "abominável triste desalentador medonho",
    "desfavorável irritante angustiante",
    "vergonhoso aborrecido inaceitável desesperador",
    "cínico odioso trágico assombroso vexatório",
    "catastrófico abatido pavoroso decepcionante horrendo aterrorizante",
    "asqueroso medonho infeliz desesperador indesejável irritante mal-humorado inaceitável",
    "inaceitável incômodo detestável desanimador catastrófico desesperado",
    "irritante desmoralizante inaceitável aborrecido horrendo abominável",
    "aborrecido entediante terrível cabisbaixo horrendo",
    "vexante horrível incomodativo angustiante indesejável",
    "solitário entristecido triste assustador deprimente catastrófico desgraçado vergonhoso",
    "chato aborrecido incomodativo repelente desconsolado",
    "desapontante vexatório nefasto",
    "cabisbaixo catastrófico vexatório irritante vexante desalentador desgraçado terrível",
    "desesperado terrível melancólico",
    "desconfortável miserável apavorante asqueroso isolado desagradável",
    "desastroso mal-humorado nojento melancólico",
    "desgraçado vexante terrífico infernal",
    "repelente desagradável desapontante irritante desalentador cabisbaixo desanimador",
    "entediante vexatório horrendo decepcionante mal-humorado",
    "terrível horrendo aborrecido miserável",
    "aborrecido mísero aborrecido",
    "decepcionante enfadonho abatido frustrante infernal triste desesperado",
    "desalentador abafado assustador nefasto doloroso",
    "inaceitável desinteressante desapontante",
    "desalentador nefasto irritante pavoroso ruim desalentador repelente desagradável",
    "aborrecido aterrorizante cínico miserável irritante chato derrotista",
    "terrível isolado desconfortável triste repugnante entristecido apavorante asqueroso",
    "vergonhoso desesperador assustador inaceitável detestável péssimo medonho",
    "irritante desesperado vexante isolado trágico ruim odioso péssimo",
    "aterrorizante desinteressante horrendo desesperado insuportável mal-humorado melancólico desesperador",
    "entediante deprimido asqueroso",
    "medonho solitário desalentador vergonhoso inaceitável aborrecido",
    "enfadonho desconsolado abafado mal-humorado inaceitável incômodo aborrecido",
    "frustrante abatido medonho terrível terrífico",
    "desesperado desastroso apavorante entristecido melancólico vexatório desesperador",
    "desinteressante embaraçoso melancólico infeliz vexante desagradável",
    "desconsolado desastroso horrível péssimo",
    "desagradável desesperador desesperado inaceitável",
    "doloroso desesperador horrível chato miserável",
    "medonho incomodativo inaceitável terrífico",
    "entristecido insatisfatório desalentador nefasto",
    "repugnante isolado pavoroso asqueroso desesperador frustrante desfavorável",
    "mal-humorado angustiante desanimador",
    "insatisfatório incomodativo irritante doloroso",
    "cínico indesejável ruim repelente",
    "melancólico pavoroso lamentável infeliz miserável",
    "desfavorável insatisfatório vexante desalentador asqueroso",
    "embaraçoso repugnante triste",
    "miserável desapontante desalentador",
    "entediante ruim vexatório desalentador odioso assustador",
    "vergonhoso assustador insuportável desalentador",
    "vexatório inaceitável desfavorável triste assombroso",
    "desesperado frustrante miserável nefasto melancólico decepcionante desalentador odioso",
    "infernal vergonhoso trágico vexatório incomodativo deprimente assombroso",
    "mal-humorado aterrorizante irritante",
    "nojento pavoroso deprimente",
    "desconsolado triste incômodo terrífico entristecido",
    "desinteressante desesperado vexante detestável",
    "desapontante vexatório desagradável terrível nefasto desgraçado horrível trágico",
    "desanimador apavorante assustador chato abatido irritante pavoroso",
    "triste irritante desesperador",
    "terrível aborrecido aterrorizante insatisfatório trágico",
    "vexatório miserável nojento irritante desinteressante",
    "abominável desmoralizante apavorante desconsolado incomodativo",
    "péssimo entediante angustiante"
]

rotulos_treinamento = [
    "positivo","positivo","positivo","positivo","positivo","positivo","positivo","positivo",
    "positivo","positivo","positivo","positivo","positivo","positivo","positivo","positivo",
    "positivo","positivo","positivo","positivo","positivo","positivo","positivo","positivo",
    "positivo","positivo","positivo","positivo","positivo","positivo","positivo","positivo",
    "positivo","positivo","positivo","positivo","positivo","positivo","positivo","positivo",
    "positivo","positivo","positivo","positivo","positivo","positivo","positivo","positivo",
    "positivo","positivo","positivo","positivo","positivo","positivo","positivo","positivo",
    "positivo","positivo","positivo","positivo","positivo","positivo","positivo","positivo",
    "positivo","positivo","positivo","positivo","positivo","positivo","positivo","positivo",
    "positivo","positivo","positivo","positivo","positivo","positivo","positivo","positivo",
    "positivo","positivo","positivo","positivo","positivo","positivo","positivo","positivo",
    "positivo","positivo","positivo","positivo","positivo","positivo","positivo","positivo",
    "positivo","positivo","positivo","positivo", "positivo",
    "negativo","negativo","negativo","negativo","negativo","negativo","negativo","negativo",
    "negativo","negativo","negativo","negativo","negativo","negativo","negativo","negativo",
    "negativo","negativo","negativo","negativo","negativo","negativo","negativo","negativo",
    "negativo","negativo","negativo","negativo","negativo","negativo","negativo","negativo",
    "negativo","negativo","negativo","negativo","negativo","negativo","negativo","negativo",
    "negativo","negativo","negativo","negativo","negativo","negativo","negativo","negativo",
    "negativo","negativo","negativo","negativo","negativo","negativo","negativo","negativo",
    "negativo","negativo","negativo","negativo","negativo","negativo","negativo","negativo",
    "negativo","negativo","negativo","negativo","negativo","negativo","negativo","negativo",
    "negativo","negativo","negativo","negativo","negativo","negativo","negativo","negativo",
    "negativo","negativo","negativo","negativo","negativo","negativo","negativo","negativo",
    "negativo","negativo","negativo","negativo","negativo","negativo","negativo","negativo",
    "negativo","negativo","negativo","negativo"
]

# =====================================================================
# 2. TREINAMENTO DO MODELO NAIVE BAYES
# =====================================================================
print("⏳ Treinando o modelo...")
vectorizer = CountVectorizer()
X_treinamento = vectorizer.fit_transform(documentos_treinamento)

classifier = MultinomialNB()
classifier.fit(X_treinamento, rotulos_treinamento)
print("✅ Modelo Naive Bayes treinado com sucesso!\n")

# =====================================================================
# 3. BUSCA DE INFORMAÇÕES NA WEB (Conforme pedido no diagrama)
# =====================================================================
print("⏳ Buscando títulos de notícias na web (G1)...")
url = 'https://g1.globo.com/rss/g1/brasil/'
response = requests.get(url)

frases_coletadas = []

if response.status_code == 200:
    root = ET.fromstring(response.content)
    
    # Extrair exatamente 30 registros
    for item in root.findall('.//item')[:30]:
        titulo = item.find('title').text
        if titulo:
            frases_coletadas.append(titulo)
            
    print(f"✅ {len(frases_coletadas)} frases coletadas com sucesso!\n")
else:
    print("❌ Erro ao acessar a fonte de dados.")

# =====================================================================
# 4. APLICAÇÃO DO ALGORITMO E VALIDAÇÃO DA BASE
# =====================================================================
if frases_coletadas:
    # Transforma as novas frases em matriz de contagem usando o padrão aprendido
    X_coletado = vectorizer.transform(frases_coletadas)
    
    # Realiza a predição (Análise de Sentimento)
    previsoes_web = classifier.predict(X_coletado)
    
    print("=" * 60)
    print("      RESULTADO DA ANÁLISE DE SENTIMENTO (DADOS DA WEB)     ")
    print("=" * 60)
    
    # Exibe o Positivo ou Negativo lado a lado com a frase extraída
    for frase, sentimento in zip(frases_coletadas, previsoes_web):
        if sentimento == 'positivo':
            print(f"[ 🟢 POSITIVO ]  -  {frase}")
        else:
            print(f"[ 🔴 NEGATIVO ]  -  {frase}")
            
    print("=" * 60)