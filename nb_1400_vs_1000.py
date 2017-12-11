import numpy as np
num_ft=6
#1000
x1_100=np.array([4.214223964 ,4.229547187 ,4.240449985 ,4.115718079 ,4.125796959 ,4.281016522 ,4.237907334 ,4.058622404 ,4.618448229 ,4.105187661 ,4.052479789 ,4.351127869 ,4.088946355 ,4.184830611 ,4.176152705 ,4.220525442 ,4.181675914 ,4.369386258 ,4.284270072 ,4.453609221 ,4.191572758 ,4.311098358 ,4.183403473 ,4.033502591 ,4.156087664 ,4.492966845 ,4.394736842 ,4.425246695 ,4.122130449 ,4.099898523 ,4.355157796 ,4.236233894 ,4.155416214 ,4.044800877 ,4.079529854 ,4.069138785 ,4.150757988 ,4.170145088 ,4.024695433 ,4.218204942 ,4.149403341 ,4.290598291 ,4.022078804 ,4.504852897 ,4.12337011 ,4.738095238 ,4.100270479 ,4.053055254 ,4.085440619 ,4.130828987 ,3.962068372 ,4.053837763 ,4.120272727 ,4.432713755 ,4.305309735 ,4.167728238 ,4.476730113 ,4.233324183 ,4.125491947 ,4.399955701 ,4.220279489 ,4.286168062 ,4.342799983 ,4.351487024 ,4.182510121 ,4.270116054])
#DET
x2_100=np.array([19.93256873 ,18.38676271 ,21.10571891 ,14.76166393 ,16.74227563 ,18.85009048 ,20.4092749 ,15.38744458 ,29.38852322 ,17.50670145 ,18.01025406 ,18.50896342 ,18.16690461 ,20.46107285 ,20.96851014 ,20.3801447 ,19.12078532 ,23.0418127 ,20.8938923 ,29.74300831 ,17.88339049 ,20.21455059 ,19.7075258 ,15.30126158 ,17.04361386 ,32.36084773 ,21.58377595 ,27.05269037 ,17.51271274 ,16.79445259 ,23.03344324 ,20.69212554 ,21.86870081 ,19.3885395 ,17.64304802 ,20.03670675 ,21.923849 ,19.44815376 ,14.45276709 ,20.11264535 ,18.56801909 ,20.6669469 ,9.612771739 ,27.45677889 ,15.50484788 ,28.57142857 ,20.22797527 ,16.09682442 ,20.20900753 ,18.6511662 ,9.024369241 ,16.2411269 ,18.31363636 ,25.72490706 ,21.43559489 ,18.89596603 ,24.45813621 ,21.83639857 ,18.42764894 ,22.81740055 ,19.49798 ,21.78024834 ,22.14152133 ,22.30536086 ,19.40890688 ,21.26692456])
#conj
x3_100=np.array([15.17555825 ,16.50677683 ,17.41893192 ,17.10980258 ,18.60593428 ,15.46355377 ,15.73685807 ,18.82155822 ,12.69766963 ,14.90826331 ,14.33769442 ,19.77244162 ,12.5142672 ,14.16880269 ,13.90023631 ,17.52164631 ,13.67193057 ,16.92069443 ,16.76608138 ,17.88548753 ,15.38461538 ,17.83948437 ,15.57563557 ,13.91404491 ,16.01790835 ,14.32262905 ,12.07146306 ,12.3254515 ,23.4443432 ,18.98184688 ,20.25435704 ,17.30031515 ,13.75430661 ,14.99566197 ,16.24753144 ,16.12873249 ,15.55336692 ,14.80967456 ,16.64172957 ,16.96947674 ,15.3221957 ,17.92069497 ,17.62907609 ,10.41856233 ,19.51061518 ,25 ,15.91962906 ,15.16066626 ,15.45033581 ,18.15821047 ,24.81270989 ,17.29087948 ,17.45151515 ,15.0929368 ,15.83087512 ,16.1358811 ,13.41181648 ,13.36810321 ,14.84837624 ,16.16815806 ,16.69646996 ,15.07363558 ,15.9222372 ,15.45747301 ,16.68825911 ,14.05222437])
#verbs
x4_100=np.array([14.31873923 ,16.01743425 ,14.81481481 ,19.52386973 ,16.9139284 ,15.40528042 ,13.30978528 ,15.49710191 ,6.947671969 ,16.0133508 ,14.27001478 ,15.47264669 ,12.4223544 ,13.91556777 ,13.86085109 ,13.86846163 ,14.82429933 ,12.98394327 ,13.15634714 ,14.70143613 ,12.88584027 ,15.21719936 ,15.49647035 ,14.40611422 ,14.70010229 ,12.00325088 ,12.96475133 ,12.08341091 ,14.5468975 ,16.29834254 ,12.76495525 ,14.41810565 ,16.14823443 ,17.73109584 ,15.72381124 ,15.3112938 ,14.38996782 ,14.58161413 ,14.86338073 ,13.82630814 ,19.37947494 ,14.92223623 ,24.17346014 ,6.642402184 ,11.26295553 ,7.142857143 ,16.53786708 ,15.64478837 ,15.57961882 ,14.21074573 ,14.1565487 ,14.22066938 ,16.50909091 ,11.52416357 ,14.25762045 ,14.64968153 ,11.71746067 ,14.3151249 ,15.42631514 ,12.7731018 ,16.14014173 ,14.15680046 ,13.13878137 ,13.16537223 ,15.90283401 ,14.38104449])
#ADJ
x5_100=np.array([5.612548748 ,5.613783529 ,5.117306859 ,4.476816646 ,4.15644924 ,5.032090436 ,5.933527041 ,4.885540897 ,10.59537296 ,5.282222035 ,5.017797401 ,4.604088113 ,5.470130222 ,6.58565208 ,6.842953709 ,5.79112798 ,4.709062456 ,5.632080854 ,5.785656277 ,7.917611489 ,7.251347379 ,5.69044676 ,5.289985114 ,5.213840758 ,4.736489092 ,7.339487778 ,4.345726702 ,7.838391361 ,5.670027336 ,5.10767843 ,6.076307113 ,7.012658853 ,4.949341764 ,4.588426215 ,4.704855631 ,4.93317447 ,5.054562118 ,5.501958019 ,4.819851365 ,5.922965116 ,7.064439141 ,5.114193639 ,2.864583333 ,9.212920837 ,6.185222334 ,7.142857143 ,4.173106646 ,4.824234417 ,4.963776365 ,5.080721899 ,5.261345044 ,5.28164672 ,4.783333333 ,8.921933086 ,7.32546706 ,4.670912951 ,6.986467158 ,5.10568213 ,5.399580471 ,6.514574289 ,4.202265051 ,6.627201848 ,7.05432088 ,6.184883501 ,4.842105263 ,5.618955513])
#NSUFF
x6_100=np.array([9.673794018 ,10.49013918 ,11.63024286 ,7.949352456 ,7.926679745 ,8.085560239 ,9.016935309 ,9.848727362 ,15.25012406 ,9.353976592 ,8.452881535 ,17.88053185 ,9.930726375 ,8.748957722 ,8.850684204 ,9.239710592 ,8.550291649 ,11.14190236 ,10.34473102 ,10.81821618 ,12.00391965 ,8.904291012 ,9.664470601 ,6.983196357 ,10.7049315 ,12.67009815 ,12.65089329 ,10.38912679 ,10.81684842 ,9.04837073 ,15.12011305 ,9.572309332 ,9.286397725 ,8.04132146 ,9.331891963 ,7.999814143 ,9.53973579 ,8.988131855 ,9.555944951 ,8.521075581 ,5.298329356 ,11.06907664 ,6.884057971 ,15.57476494 ,11.39251087 ,10.71428571 ,7.670015456 ,10.1023923 ,8.669076155 ,9.710495915 ,10.26005339 ,9.113559831 ,8.63030303 ,12.34200743 ,14.25762045 ,8.067940552 ,12.33359005 ,9.813340653 ,8.505855186 ,11.24922477 ,9.411219286 ,10.0996246 ,11.20340973 ,9.954536844 ,8.995951417 ,10.71566731])

#1400
x1_1000=np.array([4.421214326 ,4.316939245 ,4.797609233 ,4.905597723 ,4.776588404 ,4.580233193 ,4.638815384 ,4.49992829 ,4.210562834 ,4.363763261 ,4.507231556 ,4.358091118 ,4.298482964 ,4.29312763 ,4.014690451 ,4.08343014 ,4.378084667 ,4.134165995 ,4.206054169 ,4.360927152 ,4.163467902 ,4.250984806 ,4.196310573 ,4.243856488 ,4.089964158 ,4.556271845 ,4.252486016 ,4.176779228 ,4.324514382 ,4.357655779 ,4.111129572 ,4.161814633 ,4.33962588 ,4.203823301 ,4.42559771 ,4.314190744 ,4.381500743 ,4.273464391 ,4.131224335 ,4.204981436 ,4.34527439 ,4.312333037 ,4.135079126 ,4.116030781 ,4.339191232 ,4.251762146 ,4.264378122 ,4.202327952 ,4.079241937 ,4.265869715 ,4.28341399 ,4.32518485 ,4.163427211 ,4.363734919 ,4.26646654 ,4.203988969 ,4.340293415 ,4.324426631 ,4.408713693 ,4.426810865 ,4.234004097 ,4.145788137 ,4.316935641 ,4.285119699 ,4.054042179 ,4.199273279 ,4.147182829 ,4.23986347 ,4.317338452 ,4.551417271 ,4.159284587 ,4.396808198 ,4.440594059 ,4.254333134 ,4.02687398 ,4.27247969 ,4.173132184 ,4.154133776 ,4.000592373 ,4.558477537 ,4.249095066 ,4.28295912 ,4.194382236 ,4.27850516 ,4.107781558 ,4.175697211 ,4.213187903 ,4.20854539 ,4.243950541 ,4.129271117 ,4.195826446 ,4.325413661 ,4.281099237 ,4.173510563 ,4.044658339 ,4.336040609 ,4.253119664 ,4.299465653 ,4.073302559 ,4.274670927])
x2_1000=np.array([18.68380629 ,18.26769794 ,32.23413026 ,32.8115117 ,27.84626 ,25.23202309 ,28.39018378 ,23.59447831 ,18.67270724 ,16.91792295 ,26.37691746 ,19.43490604 ,21.49714001 ,21.17812062 ,13.54931794 ,14.83605843 ,20.78988126 ,18.1663533 ,18.92370331 ,22.03826343 ,16.85587741 ,18.90827237 ,18.55726872 ,18.48378113 ,15.69892473 ,23.82135922 ,18.19453076 ,17.87468048 ,21.49444007 ,22.2724114 ,14.07862765 ,17.8068262 ,22.29277501 ,18.80650995 ,22.1360287 ,20.79263615 ,19.83655275 ,17.27759838 ,19.29125475 ,18.17759901 ,20.73170732 ,18.81121995 ,17.40015072 ,16.55653326 ,20.07612569 ,21.06059889 ,19.09824516 ,19.04199968 ,16.40622114 ,17.69175466 ,18.43378795 ,17.4966048 ,20.51808289 ,22.66829865 ,20.50066709 ,18.84018223 ,21.67178437 ,22.17768871 ,22.02627939 ,21.68008048 ,18.62875045 ,18.80920974 ,18.71281353 ,20.39225002 ,16.69595782 ,17.84605478 ,17.74626294 ,19.48856286 ,18.41010877 ,23.60017837 ,19.25302472 ,20.32685492 ,22.81728173 ,20.26573491 ,15.49572896 ,19.52548006 ,18.11781609 ,19.4848359 ,13.5801555 ,24.96520007 ,20.28005334 ,19.28079435 ,18.05655722 ,21.05017567 ,15.86844631 ,17.09163347 ,19.8810114 ,17.52870162 ,17.00593942 ,18.41346402 ,19.12114582 ,20.69014284 ,18.89465649 ,16.37194398 ,16.65664036 ,17.12351946 ,20.85905688 ,19.49082875 ,16.87582639 ,20.53564635])
x3_1000=np.array([15.38523729 ,17.54738147 ,11.87139324 ,13.88361796 ,14.1581038 ,13.18632039 ,13.35955341 ,15.2474005 ,15.82384392 ,14.8241206 ,13.62308254 ,16.18493984 ,13.93185775 ,15.76838309 ,16.09391396 ,14.92173206 ,16.84305627 ,14.4686185 ,15.38325367 ,22.73730684 ,14.88570992 ,18.00787845 ,16.13436123 ,17.41890564 ,14.26523297 ,19.09902913 ,16.15910503 ,15.4320261 ,15.66972616 ,17.66272875 ,14.83042927 ,15.0727395 ,14.50145873 ,16.09403255 ,16.6404552 ,19.93863462 ,20.30089153 ,14.89656151 ,10.99619772 ,15.32075083 ,15.04573171 ,16.56277827 ,15.42012057 ,14.77712849 ,15.38440773 ,15.41700175 ,16.47239657 ,15.88263691 ,13.77221176 ,17.00241059 ,15.4641443 ,17.71540667 ,14.17829364 ,14.41860465 ,15.78540833 ,15.450016 ,15.62606619 ,14.11712314 ,19.64038728 ,20.67404427 ,15.94770454 ,14.62351056 ,16.28621427 ,16.91591102 ,12.60984183 ,14.89317664 ,14.44998084 ,15.2660409 ,23.0806142 ,14.08449339 ,15.29721199 ,16.74002844 ,14.19141914 ,15.84754724 ,14.2384106 ,16.67282127 ,15.86206897 ,13.91773993 ,15.12032581 ,15.80667613 ,17.28900743 ,17.03551302 ,15.33877396 ,16.05182257 ,15.06586408 ,16.53386454 ,18.39365394 ,16.62918689 ,17.24545969 ,15.64779373 ,15.87823312 ,19.968887 ,16.84274809 ,15.87942084 ,13.28426342 ,17.83417936 ,18.35019046 ,16.98864512 ,15.47240715 ,15.83352355])
x4_1000=np.array([16.52518393 ,16.39015174 ,8.944765045 ,8.665401645 ,14.08537381 ,12.77881766 ,13.4538007 ,14.23628541 ,17.32174197 ,16.94584031 ,11.78962747 ,16.91766933 ,13.54886844 ,15.44780605 ,18.28436516 ,19.06092992 ,14.726381 ,14.0299042 ,16.51619756 ,13.06107432 ,17.29878328 ,13.05571187 ,18.6123348 ,14.91235256 ,18.2078853 ,10.38446602 ,17.43318832 ,15.38409794 ,15.37959597 ,15.11466296 ,16.96122614 ,17.82978793 ,15.29088725 ,15.21570654 ,14.91403227 ,14.85553567 ,15.04457652 ,16.05869203 ,14.64638783 ,16.21802805 ,13.38414634 ,17.69813001 ,16.77091183 ,17.68363117 ,14.19933053 ,15.54472775 ,18.18880492 ,16.63358901 ,14.43717906 ,15.6617844 ,15.31896172 ,15.51984307 ,16.13403929 ,13.58629131 ,16.35594411 ,16.00158462 ,15.83759809 ,14.11712314 ,13.41632089 ,14.28571429 ,15.99590312 ,16.42991856 ,17.01341629 ,14.75223597 ,14.32337434 ,16.89165881 ,17.66960521 ,16.56527843 ,13.70761356 ,14.32393656 ,16.72803787 ,16.37886278 ,13.71137114 ,14.09590364 ,19.88194644 ,15.78194239 ,17.35632184 ,15.80113558 ,18.28211773 ,13.00630493 ,14.15507716 ,16.73673853 ,17.99962042 ,15.81713878 ,16.57070575 ,17.64940239 ,15.76598909 ,18.23884483 ,18.04376533 ,17.2577826 ,16.39419448 ,14.59482393 ,17.07480916 ,17.92072158 ,15.45702254 ,18.54483926 ,15.46039669 ,15.36505164 ,17.91041314 ,13.99223921])
x5_1000=np.array([5.586547013 ,4.924130602 ,10.30502885 ,11.36938646 ,9.960278239 ,9.302370925 ,9.178236126 ,7.889924704 ,6.379331456 ,4.410943607 ,9.094229364 ,5.345410301 ,7.11763243 ,5.730314566 ,3.751311647 ,4.365361717 ,5.325245225 ,4.458769809 ,4.77960701 ,4.304635762 ,4.989054625 ,4.164321891 ,3.744493392 ,5.721657929 ,4.480286738 ,6.198058252 ,4.614667495 ,5.117381945 ,5.882955661 ,4.945564049 ,3.667628917 ,4.907250988 ,5.302900292 ,4.804959959 ,6.882719867 ,4.4847865 ,4.27191679 ,5.276604805 ,6.971863118 ,4.91439769 ,5.914634146 ,5.654496883 ,4.822908817 ,4.53472175 ,6.411294677 ,5.757131369 ,5.097988984 ,5.085018506 ,5.947763124 ,5.359685355 ,5.43774747 ,5.228610231 ,4.844523395 ,6.431194265 ,5.815953936 ,4.273894958 ,5.588536336 ,6.958361167 ,5.117565698 ,5.130784708 ,5.621159176 ,5.32546959 ,5.117635621 ,4.508086671 ,5.316344464 ,5.296322701 ,5.059409736 ,5.205207961 ,3.982725528 ,9.028073985 ,4.986849027 ,6.236879529 ,6.01560156 ,5.585950071 ,3.685574431 ,5.654542097 ,3.620689655 ,5.345520011 ,3.798593114 ,6.525328893 ,5.439131263 ,5.125682082 ,4.558739799 ,5.777887571 ,4.492715694 ,4.342629482 ,4.809122459 ,3.562551781 ,4.512013171 ,5.064495431 ,5.33828911 ,4.355819545 ,5.551145038 ,4.11227154 ,4.724158675 ,5.076142132 ,3.861815316 ,4.39038175 ,4.138346981 ,5.866240584])
x6_1000=np.array([10.72034926 ,10.63352424 ,20.48639736 ,22.92852625 ,17.77595435 ,16.57307752 ,16.00391489 ,13.47077806 ,7.860903637 ,9.268565047 ,15.42731921 ,12.24280114 ,12.35016165 ,11.30034061 ,8.519150052 ,7.423474574 ,11.49974187 ,9.48160086 ,9.55921402 ,8.646063282 ,9.051570534 ,11.53629713 ,7.874449339 ,11.01326999 ,11.1827957 ,14.67184466 ,9.493474208 ,8.776738867 ,11.46068143 ,10.12277044 ,9.258374696 ,7.398599334 ,8.838167153 ,11.03074141 ,12.05845452 ,11.38327793 ,10.71693908 ,9.939320819 ,12.11863118 ,9.900990099 ,12.72865854 ,12.02137133 ,8.845139412 ,8.553883264 ,11.96145125 ,9.91532239 ,9.184065582 ,10.07348603 ,6.753112416 ,10.78562668 ,10.68191817 ,10.26859816 ,8.787058276 ,13.00227312 ,10.27666596 ,9.001843641 ,11.42954623 ,12.90358495 ,12.96680498 ,11.64486922 ,9.820460296 ,9.141601893 ,9.632510208 ,10.09129779 ,6.370826011 ,10.01770807 ,7.014181679 ,9.312119794 ,9.724888036 ,15.83136221 ,7.04892162 ,12.16225367 ,13.65136514 ,11.47993196 ,6.152221902 ,9.582717873 ,7.916666667 ,11.60504085 ,7.500925583 ,14.74493695 ,9.878072014 ,10.49109938 ,8.282406529 ,10.68291612 ,7.454418564 ,8.804780876 ,10.01487357 ,10.90069831 ,10.20962311 ,8.828019559 ,10.16730525 ,10.84712205 ,10.01526718 ,8.010918585 ,9.604019958 ,10.69373942 ,9.496913175 ,11.59636233 ,7.355772576 ,10.70531842])
x100=np.dstack((x1_100,x2_100,x3_100,x4_100,x5_100,x6_100)).reshape(-1,num_ft)
x1000=np.dstack((x1_1000,x2_1000,x3_1000,x4_1000,x5_1000,x6_1000)).reshape(-1,num_ft)
x100test=x100[-13:]
x1000test=x1000[-20:]
x100=x100[:13]
x1000=x1000[:20]

X=np.concatenate((x100,x1000),axis=0)
y100 = np.repeat(100,len(x100))
y1000=np.repeat(1000,len(x1000))
Y=np.concatenate((y100,y1000),axis=0)

#X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])


from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
print(clf.score(x100test,np.repeat(100,len(x100test))))
print(x100test)
print(clf.predict(x100test))
print(x1000test)
print(clf.predict(x1000test))