

# List of common English words (shuffled)
common_english_words = """
the be and of a in to have it I that for you he with on do say this they at but we his from
that not by she or as what go their can who get if would her all my make about know will as up
one time there year so think when which them some me people take out into just see him your come
could now than like other how then its our two more these want way look first also new because day
more use no man find here thing give many well only those tell one very her even back any good
woman through us life child there work down may after should call world over school still try in
as last ask need too feel three when state never become between high really something most another
much family own out leave put old while mean on keep student why let great same big group begin
seem country help talk where turn problem every start hand might American show part about against
place over such again few case most week company where system each right program hear so question
during work play government run small number off always move like night live Mr point believe hold
today bring happen next without before large million must home under water room write mother area
national money story young fact month different lot right study book eye job word though business
issue side kind four head far black long both little house yes after since long provide service
around friend important father sit away until power hour game often yet line political end among
ever stand bad lose however member pay law meet car city almost include continue set later community
name five once white least president learn real change team minute best several idea kid body
information nothing ago lead social understand whether watch together follow parent stop face
create speak read allow add office spend door health person sure art war history party within grow
result open change morning walk reason low win research girl guy early food before moment himself
air teacher force offer enough both education across although remember foot second boy maybe toward
able age policy everything love process music including consider appear actually buy probably human
wait serve market die send expect home sense build stay fall oh nation plan cut college interest
death course someone experience behind reach local kill six remain effect use yeah suggest class
control raise care perhaps little late hard field else pass former sell major sometimes require
along development themselves report role better economic effort up decide rate strong possible
heart drug leader light voice wife whole police mind finally pull return free military price less
according decision explain son hope develop view relationship carry town road drive arm true federal
break better difference thank receive value international building action full model join season
society tax director position player agree especially record pick wear paper special space ground form
support event official whose matter everyone center couple site end project hit base activity star table
court produce eat teach oil half situation easy cost industry figure face street image itself phone
either cover quite picture clear practice piece land recent describe product doctor wall patient worker news
test movie certain north love personal open support simple third technology catch step baby computer type attention
draw film Republican tree source red organization choose cause hair look point century evidence window difficult listen
soon culture billion chance brother energy period summer realize hundred available plant likely opportunity term short letter condition
choice place single rule daughter administration south husband Congress floor campaign material population well call economy medical hospital
church close thousand risk current fire future wrong involve defense anyone increase security bank myself certainly west sport board seek per subject officer
private rest behavior deal performance fight throw top quickly past goal second bed order author fill represent focus foreign drop blood upon agency push nature color no recently store reduce sound note fine before near movement page enter share common poor other natural race concern series significant similar hot language each usually response dead rise animal factor decade article shoot east save seven artist away scene stock career despite central eight thus treatment beyond happy exactly protect approach lie size dog fund serious occur media ready sign thought list individual simple quality pressure accept answer hard resource identify left meeting determine prepare disease whatever success argue cup particularly amount ability staff recognize indicate character growth loss degree wonder attack herself region television box TV training pretty trade deal election everybody physical lay general feeling standard bill message fail outside arrive analysis benefit sex forward lawyer present section environmental glass skill sister PM professor operation financial crime stage compare authority miss design sort act ten knowledge gun station blue state strategy little clearly discuss indeed force truth song example democratic check environment leg dark public various rather laugh guess executive prove hang entire rock design enough forget since claim remove manager enjoy network legal religious cold final main science green memory card above seat cell establish nice trial expert spring firm Democrat radio visit management care avoid imagine tonight huge ball no close finish yourself talk theory impact respond statement maintain charge popular traditional onto reveal direction weapon employee cultural contain peace head control base pain apply play measure wide shake fly interview manage chair fish particular camera structure politics perform bit weight suddenly discover candidate top production treat trip evening affect inside conference unit best style adult worry range mention rather deep edge specific writer trouble necessary throughout challenge fear shoulder institution middle sea dream bar beautiful property instead improve stuff detail method sign somebody magazine hotel soldier reflect heavy sexual cause bag heat fall marriage tough sing surface purpose exist pattern whom skin agent owner machine gas down ahead generation commercial address cancer test item reality coach Mrs yard beat violence total tend investment discussion finger garden notice collection modern task partner positive civil kitchen consumer shot budget wish painting scientist safe agreement capital mouth nor victim newspaper threat responsibility smile attorney score account interesting audience rich dinner figure vote western relate travel debate prevent citizen majority none front born admit senior assume wind key professional mission quick anyway speech option participant southern fresh eventually nose afraid solution abroad insurance department battle date initial pride nod block electronic encourage link massive challenge big enough
""".split()

def is_plausible_english(text, threshold=0.5):
    words_in_text = text.split()
    if not words_in_text:
        return False
    english_word_count = sum(1 for word in words_in_text if word.lower() in common_english_words)
    return english_word_count / len(words_in_text) > threshold  # More than `threshold` of words are English


