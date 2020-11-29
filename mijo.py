import time
import json
import requests
import uuid
import random

def get_mijo_message():
  uid = uuid.uuid4().hex
  mijo_message = "¡Hola!\n ¿Quieres ofrecer o necesitas lentes certificados para el eclipse solar para tus huéspedes?\n Compra con el cupón descuento AIRBNBPREV en http://host.miraeleclipse.cl/\n Mira nuestra oferta comercial completa en: https://drive.google.com/file/d/1_u7vhtU7HO6dVinTYJDgtM96u-2ZfRB4/view?usp=sharing&hash={}\n ¡Despachamos en La Araucanía y Los Ríos!"
  mijo_message = mijo_message.format(uid)
  return mijo_message

def send_mijo_message_to(listing_id):
  user_id = 55975833
  url_key = "d306zoyjsyarp7ifhu67rjxn52tv0t20"
  url = "https://www.airbnb.cl/api/v2/threads?_format=for_contact_host_standalone&currency=CLP&key={}&locale=es-X L".format(url_key)
  payload = {
      "user_id": user_id,
      "listing_id": listing_id,
      "number_of_adults": 1,
      "number_of_children": 0,
      "number_of_infants": 0,
      "checkin_date": "2021-03-11",
      "checkout_date": "2021-03-17",
      "message": get_mijo_message(),
      "is_open_homes": False
  }

  payload = json.dumps(payload)

  headers = {
    'authority': 'www.airbnb.cl',
    'device-memory': '8',
    'x-airbnb-supports-airlock-v2': 'true',
    'x-csrf-without-token': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
    'viewport-width': '1920',
    'content-type': 'application/json',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'cache-control': 'no-cache',
    'x-csrf-token': 'V4$.airbnb.cl$KVhNM-vNIBY$8JHf96dFnozClKuoGIDsdPYuUxfAgPo1X5ED_6WYwqo=',
    'x-requested-with': 'XMLHttpRequest',
    'dpr': '1',
    'ect': '4g',
    'origin': 'https://www.airbnb.cl',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.airbnb.cl/contact_host/45465926/send_message?adults=1&check_in=2021-01-04&check_out=2021-01-31',
    'accept-language': 'es-CL,es;q=0.9',
    'cookie': 'bev=1606666369_MWJjOWIyY2U1MGMy; cdn_exp_da1663c66e2988797=treatment_2; jitney_client_session_id=c20284a1-efbc-4142-9080-be11566c8734; jitney_client_session_created_at=1606666370; flags=0; frmfctr=wide; cfrmfctr=DESKTOP; __ssid=48e5874f5d92136386b04ce37fefb9e; auth_jitney_session_id=d0d963b9-cf9e-4e19-9ffe-f177c79abcac; auth_merge_email=jose.pradenas.fuentes%40gmail.com; __svt=409; _csrf_token=V4%24.airbnb.cl%24KVhNM-vNIBY%248JHf96dFnozClKuoGIDsdPYuUxfAgPo1X5ED_6WYwqo%3D; li=1; _pt=1--WyI3MzJiYmQzYzI5NGQyNGI5OGEwYTcyNGExNDc5ZDk0YmNkNTQyNjIwIl0%3D--fedbf26750af2a05054b3190c7e58425eb81471c; _aat=0%7CLo4RwvLYb6QOAQZksj1REr%2FAsSfNcViYP4RlZAMsl0X0N5wIBWtCnK7HtazCHaEo; abb_fa2=%7B%22user_id%22%3A%2245%7C1%7C5SWbUM%2B5npb6R%2FXzrzuncA50HultyepTUwqbD0rlD051oC5BzUFT1Sc%3D%22%7D; alfc=0; alfces=0; jlp3=true; rclu=%7B%22377470886%22%3D%3E%22Kc0kvnwbzPci2%2Fl9Bp8%2BiDKt8l68sws%2BtY3pL1mQIrc%3D%22%7D; rclmd=%7B%22377470886%22%3D%3E%22google%22%7D; roles=0; _airbed_session_id=8454b0e2484037407a45c02447a4aceb; hli=1; previousTab=%7B%22id%22%3A%220693e289-a0fe-4803-a9de-3b5d79864844%22%2C%22url%22%3A%22https%3A%2F%2Fwww.airbnb.cl%2Frooms%2F45465926%3Fcheck_in%3D2021-01-04%26check_out%3D2021-01-31%26previous_page_section_name%3D1000%26federated_search_id%3D86a8611b-9345-49da-8733-8639c8035db1%22%7D; OptanonAlertBoxClosed=2020-11-29T16:15:17.328Z; OptanonConsent=landingPath=NotLandingPage&datestamp=Sun+Nov+29+2020+13%3A15%3A17+GMT-0300+(Chile+Summer+Time)&version=4.6.0&groups=0_179751%3A1%2C1%3A1%2C2%3A1%2C0_183217%3A1%2C3%3A1%2C0_183345%3A1%2C0_183219%3A1%2C4%3A1%2C0_183240%3A1%2C0_179739%3A1%2C0_179743%3A1%2C0_185813%3A1%2C0_183096%3A1%2C0_179755%3A1%2C0_183215%3A1%2C0_185808%3A1%2C0_179747%3A1%2C0_179740%3A1%2C0_179744%3A1%2C0_185810%3A1%2C0_185814%3A1%2C0_183097%3A1%2C0_179756%3A1%2C0_183216%3A1%2C0_183344%3A1%2C0_185809%3A1%2C0_179748%3A1%2C0_179752%3A1%2C0_183241%3A1%2C0_179741%3A1%2C0_183098%3A1%2C0_179745%3A1%2C0_183346%3A1%2C0_185811%3A1%2C0_179737%3A1%2C0_179757%3A1%2C0_179749%3A1%2C0_179753%3A1%2C0_185831%3A1%2C0_183099%3A1%2C0_179738%3A1%2C0_179742%3A1%2C0_183095%3A1%2C0_183243%3A1%2C0_179754%3A1%2C0_183214%3A1%2C0_179750%3A1%2C0_200000%3A1%2C0_200001%3A1%2C0_200002%3A1%2C0_200003%3A1%2C0_200004%3A1%2C0_200005%3A1%2C0_200006%3A1%2C0_200007%3A1%2C0_200008%3A1%2C0_200009%3A1%2C0_200010%3A1&AwaitingReconsent=false; _gcl_au=1.1.1425479071.1606666517; _ga=GA1.2.819834499.1606666517; _gid=GA1.2.22495861.1606666517; _gat=1; jitney_client_session_updated_at=1606666519; _user_attributes=%7B%22curr%22%3A%22CLP%22%2C%22guest_exchange%22%3A766.942315%2C%22device_profiling_session_id%22%3A%221606666370--41b581caf74106208d5f9f66%22%2C%22giftcard_profiling_session_id%22%3A%221606666370--06c4d5b9b92ed24d84b12d53%22%2C%22reservation_profiling_session_id%22%3A%221606666370--1c27175ef54d96ae1f673fd8%22%2C%22id%22%3A377470886%2C%22hash_user_id%22%3A%22732bbd3c294d24b98a0a724a1479d94bcd542620%22%2C%22eid%22%3A%22EejbCf7mQuwhXqe9Pczkrg%3D%3D%22%2C%22num_msg%22%3A0%2C%22num_notif%22%3A%222%22%2C%22num_alert%22%3A4%2C%22num_h%22%3A0%2C%22num_trip_notif%22%3A0%2C%22name%22%3A%22Jos%C3%A9%22%2C%22num_action%22%3A0%2C%22is_admin%22%3Afalse%2C%22can_access_photography%22%3Afalse%2C%22travel_credit_status%22%3Anull%2C%22referrals_info%22%3A%7B%22receiver_max_savings%22%3Anull%2C%22receiver_savings_percent%22%3Anull%2C%22receiver_signup%22%3Anull%2C%22referrer_guest%22%3A%22%2412%2C000%2BCLP%22%2C%22terms_and_conditions_link%22%3A%22%2Fhelp%2Farticle%2F2269%22%2C%22wechat_link%22%3Anull%2C%22offer_discount_type%22%3Anull%7D%2C%22agreed_to_community_commitment%22%3Atrue%7D'
  }
  #print(payload)
  response = requests.request("POST", url, headers=headers, data = payload)
  print(response.text.encode('utf8'))

listings = [5927376, 62519809, 225564800, 119987488, 156386381, 235704643, 227719002, 35705189, 12007210, 59222429, 49866788, 335057019, 51150139, 323348084, 14809206, 112313338, 3931956, 112309006, 243976242, 11977946, 27075454, 172140259, 177362781, 4549942, 205093616, 15598305, 103000563, 92317138, 22945595, 34753166, 242958727, 208545872, 28920300, 308282734, 20807822, 6796089, 170952201, 28069195, 41699354, 164546746, 168798349, 174490768, 25364469, 19537468, 65520027, 262520373, 138056740, 225620335, 244179341, 172698446, 93539779, 289961703, 67391975, 99008326, 30641410, 190660480, 113100987, 179847970, 311600235, 114905208, 101830914, 21320813, 333282523, 41393684, 88790983, 60613047, 237832828, 273353419, 160599124, 49797780, 22267236, 34114078, 123214261, 142921180, 244576208, 297685207, 6250071, 4657646, 11026556, 71879433, 212333841, 142071525, 176563639, 166265139, 266812191, 124676205, 202877043, 2566356, 376286242, 92475388, 234489206, 273157185, 29007586, 325723903, 333521151, 217091026, 126171843, 10799450, 10445214, 76431963, 86341286, 142303419, 296082745, 235402229, 328935170, 96187869, 155152245, 233894095, 275091032, 79716103, 232589514, 302387526, 1961556, 126246574, 151003162, 41939626, 262817261, 336286997, 5004432, 208541393, 405027, 283735638, 149438896, 244706145, 260504188, 324043983, 316099104, 20332999, 303968492, 128827045, 13784055, 238586809, 372323085, 275416510, 173332451, 121211766, 68890920, 324132471, 74226023, 207881471, 142424579, 109246011, 246056687, 56186068, 103479213, 145340800, 336548036, 123226327, 286983175, 117172655, 284875566, 239432606, 139455351, 331240287, 91961192, 233731375, 60068313, 61464897, 118803069, 235069213, 148994876, 90310554, 110769845, 91580927, 156121548, 325724972, 232560717, 808644, 172070570, 39905874, 146379705, 332600739, 53055148, 3834607, 37983414, 280773319, 5498481, 5178967, 58995805, 172397237, 242602638, 67385138, 102178055, 328238823, 335186061, 336162576, 243724650, 323588913, 27922860, 314852876, 85284581, 69674961, 44958622, 305810653, 222576919, 335671691, 243310672, 276676692, 165401851, 13448377, 318546272, 306300482, 48792033, 235335093, 21478547, 6906976, 227428963, 173958477, 109331486, 18595121, 13246617, 4428978, 48807252, 334240674, 269778114, 4036593, 169680819, 171491197, 232505533, 264236441, 316011724, 149873825, 11607974, 6577914, 97420792, 117490032, 244361944, 114197536, 244115478, 40262295, 334840669, 109394538, 272548310, 31725787, 266424182, 163321324, 53770046, 252397961, 61373138, 308450406, 45306893, 199780216, 172363303, 332409789, 235142163, 99543357, 65305490, 75534597, 130311953, 327066537, 252783854, 14212871, 55101480, 218946654, 204490780, 4272184, 5871046, 9359079, 87073709, 116101618, 53685813, 276602200, 115936168, 218498199, 166651001, 205124458, 139527883, 18464963, 158571927, 104890136, 324427389, 235975631, 85491629, 100749799, 59653266, 314846905, 3997170, 236611875, 101419358, 334397765, 48146482, 146191155, 287937131, 331098567, 66225371, 187846306, 61195711, 173267540, 241330686, 167076716, 331181513, 256503456, 141935517, 214889452, 258433552, 73300497, 219434856, 67164115, 115825026, 53189614, 2085830, 113066512, 111283589, 331406334, 338416374, 375934723, 196032954, 13136635, 227506325, 148133778, 166532186, 187173726, 31583699, 334833875, 173063359, 266261277, 276105983, 56235456, 163806448, 49084579, 242144814, 238138335, 104006636, 43969336, 32196690, 161977231, 121838933, 211949366, 113292113, 117208248, 175147954, 280207352, 70905634, 226363393, 9699202, 44958622, 1445575, 52392972, 62591869, 239823074, 115719864, 251446338, 26292554, 4981807, 9825079, 103599498, 168636001, 331130298, 212669131, 167619427, 311382689, 137688022, 327926968, 156228455, 125071747, 332634294, 335337597, 2639135, 146443, 263755627, 174367381, 325907788, 82367994, 302505518, 111204184, 169918217, 111462293, 201641063, 237012237, 230709114, 234604099, 242749003, 25886201, 165478606, 63869506, 329467131, 25011133, 4036593, 137913779, 330074152, 172162694, 209367939, 80210186, 210829223, 222959938, 166029156, 70905825, 103310293, 82904833, 165478792, 361812, 29124599, 22343551, 153862506, 24634934, 13135996, 114026066, 130321063, 528348, 43705791, 8843023, 3421543, 232963140, 40447798, 40375377, 31079116, 41885221, 3457722, 95476027, 111019430, 169106405, 336338594, 34135736, 154341966, 117982641, 233545905, 56128234, 101157545, 325676821, 42653103, 23304823, 332232421, 219362301, 124481909, 128025154, 38848601, 32721296, 234804887, 247494809, 17664051, 333926658, 153129054, 109529549, 165019450, 51228798, 33584499, 224353818, 6037429, 262876320, 242623641, 336842271, 118261048, 45033462, 120357842, 6540712, 63756690, 45077570, 248416415, 330377385, 30076427, 53855739, 84970822, 59399893, 9330136, 27147812, 57635210, 327051220, 75977322, 104066357, 178241497, 59967519, 118430964, 18459904, 341189186, 101346499, 333793561, 221768348, 340276699, 239187419, 231946575, 330716657, 242378261, 175376975, 42700745, 38548688, 179646005, 334854852, 336407853, 220204615, 52429528, 13358158, 143405445, 38268110, 290580408, 87334105, 240481841, 163368092, 160342542, 29047051, 164383096, 244638400, 268683, 78951346, 16430506, 336879257, 109004705, 25556614, 265368454, 141928336, 263517789, 17099419, 13000713, 108209142, 78719875, 124623579, 46231254, 25554234, 127103516, 184590512, 9768369, 188592752, 234359311, 235935565, 133998279, 323964408, 26850487, 227914790, 29582778, 303891159, 225588165, 329187922, 126321396, 222704246, 238344296, 52392972, 92943388, 20244699, 285050083, 140077555, 58995805, 145216593, 79383257, 190683799, 4419755, 72123266, 101780211, 47803253, 200894633, 100918669, 4225537, 82452312, 148415432, 103308107, 10170960, 225746982, 81976673, 92886840, 337183356, 140729739, 316804100, 217660753, 132071339, 9391157, 65818886, 70055308, 35062906, 70478235, 219176690, 6669090, 29652088, 114637222, 149714693, 167845595, 577676, 337858417, 133293812, 193104193, 182847271, 336954466, 10553436, 10140456, 149160965, 26288554, 108474917, 225824214, 189632855, 114160000, 295268614, 239565830, 374751227, 252873104, 224324440, 194975118, 33486397, 30344836, 85765706, 122147138, 31069743, 9452445, 236828297, 335038440, 23751604, 251178350, 229384826, 63806197, 6014257, 321625477, 216597340, 243209967, 113020345, 13445703, 327363489, 103716111, 165653312, 157362839, 108848257, 328692705, 26147391, 34203563, 211131165, 2591499, 257839721, 110208110, 112582727, 49665834, 201583902, 336937330, 34317221, 2788631, 62805984, 202563744, 171888158, 322894140, 49718672, 101214894, 198734845, 273318747, 201926297, 163015158, 113843393, 325163976, 2558722, 116844797, 92520441, 9072384, 16342912, 199906388, 153434056, 15948852, 6232041, 175902050, 334593369, 100207348, 329813001, 131357852, 69222354, 123876422, 155397982, 229908823, 3731951, 337412295, 297896115, 95413292, 324367549, 312049523, 241876519, 3126395, 132663996, 91133472, 301691117, 204618439, 152469607, 337421862, 21146029, 324866437, 168629305, 330224654, 193392034, 341371916, 320628196, 316660727, 25241112, 91616560, 187747691, 233855052, 224885594, 13060494, 143889872, 174950591, 299995146, 214305821, 11767165, 339044887, 23105763, 69583497, 28653798, 266529497, 337613350, 556989, 7695549, 150483195, 140344136, 147124178, 21775110, 97808537, 294091306, 78533700, 75241810, 61166508, 5382837, 283469169, 133736073, 56095234, 197479946, 17259599, 289857501, 198296349, 107304304, 222748968, 338776064, 251608348, 12849684, 44880111, 30016600, 90247046, 339279405, 310902315, 35621095, 170941617, 158202723, 228703319, 333735142, 22021739, 292849207, 7733388, 30469836, 191453591, 234294628, 52094055, 179851487, 297467821, 170564697, 163737323, 224887484, 63121818, 23151400, 40491119, 24204206, 2279321, 64005771, 158446071, 82164, 315384282, 328048583, 102630447, 13885397, 91133472, 33396028, 301197324, 304653214, 237793774, 154725392, 170184935, 223311783, 133241232, 337810816, 224536987, 47150003, 337106667, 280060592, 157400230, 200392611, 242040983, 170790151, 130790441, 325079385, 30246461, 300755524, 113030489, 328751582, 171841609, 287278203, 66793587, 98895581, 6931653, 191178538, 333990361, 418243, 333415278, 71555207, 136931584, 101533161, 323339454, 201834260, 194548278, 5000380, 3631527, 242558700, 210282603, 283845116, 328429945, 341028251, 278514614, 191971959, 167137850, 111657580, 127617055, 47921773, 60590128, 77306903, 244401710, 334288699, 270605904, 226864529, 191592097, 141389773, 6231767, 189595875, 197713662, 56327787, 328707912, 2649286, 37580161, 112845926, 177844055, 49698778, 168256020, 243548783, 334469323, 322981575, 230391487, 9977781, 112122427, 227698066, 118648467, 69861058, 221633336, 47748087, 241747270, 239828314, 92296444, 319328740, 181718310, 121180715, 11080715, 159353438, 173075155, 34131780, 13770439, 116211033, 20236311, 329990331, 20335354, 24231585, 141227343, 253010216, 338362814, 13693392, 324979652, 333985917, 89025600, 172438181, 141363656, 98853046, 65745411, 233697312, 232139921, 1260320, 51859113, 241430500, 327843757, 139871926, 161908495, 112671618, 160286112, 167276080, 52598086, 15929370, 179254442, 334836738, 432380, 260677366, 334726153, 57307573, 94275063, 114715383, 233196568, 168137996, 134959568, 239739763, 47108360, 18640274, 316405499, 329456710, 103335059, 74333439, 112271583, 215423905, 4225178, 331116272, 267362419, 157958445, 35208614, 86411137, 110502547, 4412924, 111770575, 59234249, 140638624, 20414122, 7250066, 68013656, 1174042, 164736048, 175306644, 41410704, 138945760, 234298275, 136989930, 16405708, 225732278, 326909469, 175306644, 140463279, 6189380, 22005369, 217444038, 18810676, 38049354, 153027711, 36651549, 68550383, 3376885, 259782032, 314640933, 12604374, 308776679, 326738172, 74642512, 108851018, 207812767, 224877826, 286784447, 175885695, 2994742, 322843784, 244625727, 329256172, 229647062, 290329618, 241492767, 4944034, 225986555, 116528726, 212222340, 102430639, 65350186, 179030318, 32046614, 231213931, 165294245, 13832728, 12497699, 332470056, 163069570, 334616085, 87371096, 322457997, 91585501, 79759345, 160908684, 306334646, 113996405, 134043262, 241502044, 224467659, 39863471, 326184461, 46578903, 66131191, 173958477, 132699833, 140103240, 164744056, 137586371, 249985394, 332645941, 15900204, 152259138, 276632984, 239823074, 327738122, 213979642, 161327089, 309611825, 229075369, 238786564, 20564513, 334530442, 328414386, 34177832, 66096822, 185033888, 185961188, 234161926, 323010262, 52935503, 10766214, 70729426, 247098114, 328837349, 228079186, 224549147, 168420412, 31244134, 10980602, 204865264, 135219740, 58330626, 58294023, 169518077, 321684396, 26214437, 270344580, 4910726, 329414976, 246434659, 250974789, 22733236, 201834260, 329313094, 7301836, 335504756, 234141348, 12270825, 5331100, 262521496, 176248389, 73981896, 114093045, 25971200, 24688459, 32519001, 328048128, 162719384, 284626908, 333882992, 338006320, 329936411, 72177250, 65630103, 19821805, 85708967, 48354033, 329053352, 152514598, 208017119, 31161573, 172478172, 54653588, 77358987, 316611213, 20416513, 332892422, 333246616, 239433506, 163062192, 235518398, 49346464, 235975379, 332895328, 36233103, 108118728, 4860380, 43269158, 2798813, 94551444, 122639411, 14690724, 219972766, 7208782, 120566220, 13419409, 271005632, 49207641, 103890659, 335839289, 165916013, 57585046, 179511616, 94785397, 226590307, 321847719, 336935817, 239870152, 87363842, 189418884, 330041497, 32738042, 277239255, 109158374, 14482498, 241103968, 174419178, 242533957, 241365085, 225405384, 8319984, 185341377, 238768843, 330413582, 279529303, 48979196, 330733470, 100112861, 113019870, 21622178, 231527388, 246697435, 31307722, 166901609, 174951101, 235301669, 77275826, 325726840, 361022546, 329647893, 152026172, 92784259, 7070951, 333357979, 2471425, 21225038, 34199595, 188205977, 24239828, 45056370, 14487765, 324962769, 232934011, 323354510, 58909451, 127758359, 241579080, 333982815, 41863936, 206517008, 241876519, 100341524, 198035594, 172694780, 8332264, 138699999, 10491636, 331217254, 162586008, 201104497, 110525616, 268411959, 145424460, 220973653, 273631877, 271349022, 237330476, 108878435, 14242397, 98991851, 109064459, 32914868, 49207641, 557511, 55811575, 110513853, 43680171, 288112742, 67569573, 98710885, 27551283, 27557321, 243801, 22246506, 109390762, 142019361, 325088737, 100551653, 35907449, 534984, 157862172, 333866518, 225537112, 24879625, 101038876, 216329029, 297219798, 36342994, 154972957, 325557446, 246189653, 28015932, 115758684, 25012905, 106364679, 318163049, 271252105, 132324452, 1585695, 22206213, 284104, 296141048, 1136091, 177716623, 29376189, 16840586, 259875201, 270860506, 243664473, 71132018, 52674423, 316594149, 157823760, 338047001, 141790729, 13186660, 15153114, 253047063, 73271508, 4759508, 338006320, 335089908, 103659803, 315339205, 2990525, 114996563, 3150638, 123787132, 298145719, 156534722, 113374732, 337724194, 318319434, 99547195, 1159876, 272829887, 299616766, 326217104, 167063950, 214026027, 233418646, 25321205, 94054787, 75317050, 154905631, 47671541, 333700411, 338144085, 858653, 18166657, 21202181, 200843828, 6793783, 316934858, 290873206, 57856914, 10791316, 2039346, 241548377, 216049156, 85190576, 329889210, 98947904, 180179056, 158484328, 231804775, 169690977, 111000211, 315105109, 59094815, 237280558, 172351948, 60219316, 182085863, 202276322, 193360333, 227037331, 99876414, 170949223, 5032304, 39250145, 2455614, 96237411, 145568539, 265894694, 74312993, 13060494, 230852281, 13608014, 335611183, 210407475, 242384028, 102137290, 46079166, 241220582, 53857273, 311906730, 331107389, 33107231, 164179102, 52520837, 101960872, 337708037, 357474865, 5596602, 144832918, 309950279, 48792033, 326328665, 232087743, 61576558, 110831320, 88498892, 76806967, 3963366, 162029352, 239828964, 170409525, 152256666, 71014298, 234494490, 261438945, 324432547, 36568294, 320953181]

listings = [5927376, 62519809, 225564800]

for listing_id in listings:
  time_to_send = random.uniform(60 * 2, 60 * 5)
  send_mijo_message_to(listing_id)
  time.sleep(time_to_send)


