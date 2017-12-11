import numpy as np
num_ft=6
#wordL
x1_100=np.array([3.846439838  ,3.820023225  ,4.138919515  ,3.874681934 ,3.815851937 ,3.886318332 ,4.108649035 ,4.05907215 ,3.88925162 ,4.039080325 ,3.851568041 ,3.945305619 ,3.880878626 ,4.164136046 ,4.010847908 ,3.847257579 ,3.654579703 ,3.855923233 ,3.775156351 ,3.736493165 ,3.740128366 ,3.937271365 ,4.0205596 ,4.046155453 ,3.74643238 ,3.862880452 ,3.857670005 ,4.21940227 ,3.750152718 ,3.949810524 ,3.877539176 ,4.092454667 ,3.818970028 ,3.753983172 ,3.827212299 ,3.894793656 ,3.886231416 ,3.901967674 ,3.814916182 ,3.842033342 ,3.724269889 ,3.873849775 ,3.843037603 ,3.793500896 ,3.912359213 ,3.972396694 ,3.823449784 ,4.044104727])
#DET
x2_100=np.array([12.21270843 ,12.26655072 ,16.40573319 ,8.905852417 ,10.25147549 ,11.33885228 ,14.86776269 ,18.02664446 ,13.03678043 ,17.08301644 ,13.63650516 ,12.61229523 ,14.33399043 ,18.12936532 ,9.34248395 ,7.775977783 ,9.606781257 ,8.773360634 ,9.954712098 ,9.736477959 ,8.774010511 ,10.82160214 ,14.50050117 ,13.51821442 ,8.206794982 ,9.925739985 ,13.17870322 ,14.68951103 ,9.835064142 ,13.26188203 ,10.44689495 ,15.706427 ,8.401225802 ,8.973326173 ,9.914961566 ,11.23474217 ,12.54501801 ,15.67111736 ,10.19500513 ,11.29634691 ,9.164149043 ,12.9681147 ,11.63631022 ,11.1904416 ,14.67187265 ,14.39669421 ,10.82417868 ,14.21542787])
#conj
x3_100=np.array([13.84632717 ,12.4579662 ,14.99448732 ,13.35877863 ,11.40620991 ,11.29429422 ,16.58327377 ,14.94044818 ,11.42604004 ,14.44450945 ,14.52837695 ,14.06552757 ,18.19205858 ,17.62830246 ,17.17954395 ,8.84054617 ,11.32564163 ,13.71705218 ,10.92948027 ,7.697337409 ,9.371657132 ,8.844220341 ,21.42907093 ,18.47154401 ,9.872530598 ,10.96119653 ,9.804955192 ,15.18206874 ,10.01832621 ,15.77569499 ,6.384213581 ,17.4608924 ,9.470065027 ,10.01611171 ,12.35471054 ,11.16831354 ,12.48961123 ,13.31693605 ,7.218611016 ,12.6172907 ,9.204431017 ,13.27840788 ,11.07814336 ,12.56165985 ,11.95374681 ,12.41322314 ,15.17155204 ,17.39588824 ])
#verbs
x4_100=np.array([12.85488959 ,22.21432149 ,21.323043 ,22.45547074 ,18.8959456 ,22.94270772 ,17.83416726 ,16.02649966 ,19.98659047 ,19.26519628 ,21.89202747 ,20.53020962 ,17.0233737 ,15.51017309 ,24.26389196 ,19.50937283 ,19.77866729 ,19.69321002 ,18.76644382 ,20.20741146 ,18.71075764 ,23.98031745 ,18.30861157 ,19.4740936 ,19.37433345 ,18.94153331 ,20.66420664 ,18.9293768 ,19.2425168 ,18.78561717 ,17.23737667 ,19.34213207 ,19.89685328 ,19.61152882 ,22.16198151 ,21.13260815 ,21.85335673 ,19.53619115 ,15.91971719 ,18.55698278 ,21.8529708 ,21.17483415 ,21.08695652 ,18.72868281 ,21.43865445 ,27.40495868 ,23.50184828 ,21.56035846 ])
#ADJ
x5_100=np.array([2.501126634 ,2.706013792 ,4.785005513 ,1.272264631 ,2.26777008 ,2.112989845 ,4.360257327 ,4.737899576 ,3.742696593 ,3.498508161 ,3.852208057 ,2.703892901 ,3.083638412 ,4.2818099 ,2.590214744 ,1.920851655 ,2.213327054 ,2.438008641 ,1.98835454 ,1.578395146 ,4.571880378 ,1.999437207 ,4.187289723 ,4.537401149 ,3.58031588 ,3.033155528 ,2.424881392 ,3.639154691 ,1.466096518 ,2.745234169 ,2.611723738 ,3.699092206 ,2.10030645 ,1.808091658 ,2.272642876 ,2.399734285 ,2.123926494 ,2.213633169 ,2.907971262 ,2.277489296 ,2.819738167 ,2.493045153 ,2.194477086 ,2.363310572 ,3.396906442 ,3.553719008 ,4.206799604 ,3.127745563 ])
#NSUFF
x6_100=np.array([8.235691753 ,7.076318527 ,7.210584344 ,6.234096692 ,5.401590967 ,5.721019676 ,11.18656183 ,9.047713862 ,7.814246033 ,7.008717019 ,8.709069208 ,6.579179144 ,7.406364404 ,7.599453386 ,6.575160505 ,4.582272622 ,8.994584413 ,6.033420674 ,6.081518223 ,3.555190609 ,8.078694014 ,5.065900051 ,8.631768701 ,6.860118405 ,5.616779239 ,5.198201025 ,5.745914602 ,8.896169595 ,6.597434331 ,7.594955018 ,5.629715612 ,7.631358522 ,5.01532252 ,5.558539205 ,6.921905752 ,5.73777298 ,5.868501247 ,6.219255095 ,4.926445433 ,5.602623668 ,5.760322256 ,5.94906912 ,6.42773208 ,6.61879164 ,6.493467488 ,9.818181818 ,7.78882699 ,7.836935512])

x1_1000=np.array([4.214223964 ,4.229547187 ,4.240449985 ,4.115718079 ,4.125796959 ,4.281016522 ,4.237907334 ,4.058622404 ,4.618448229 ,4.105187661 ,4.052479789 ,4.351127869 ,4.088946355 ,4.184830611 ,4.176152705 ,4.220525442 ,4.181675914 ,4.369386258 ,4.284270072 ,4.453609221 ,4.191572758 ,4.311098358 ,4.183403473 ,4.033502591 ,3.965676631 ,4.492966845 ,4.313282693 ,4.156087664 ,4.394736842 ,4.425246695 ,4.122130449 ,4.099898523 ,4.355157796 ,4.236233894 ,4.155416214 ,4.044800877 ,4.079529854 ,4.069138785 ,4.150757988 ,4.170145088 ,4.024695433 ,4.218204942 ,4.149403341 ,4.290598291 ,4.022078804 ,4.504852897 ,4.12337011 ,4.738095238 ,4.100270479 ,4.053055254 ,4.085440619 ,4.130828987 ,3.962068372 ,4.053837763 ,4.120272727 ,4.432713755 ,4.305309735 ,4.167728238 ,4.476730113 ,4.233324183 ,4.125491947 ,4.399955701 ,4.220279489 ,4.286168062 ,4.342799983 ,4.351487024 ,4.182510121 ,4.270116054])
x2_1000=np.array([19.93256873 ,18.38676271 ,21.10571891 ,14.76166393 ,16.74227563 ,18.85009048 ,20.4092749 ,15.38744458 ,29.38852322 ,17.50670145 ,18.01025406 ,18.50896342 ,18.16690461 ,20.46107285 ,20.96851014 ,20.3801447 ,19.12078532 ,23.0418127 ,20.8938923 ,29.74300831 ,17.88339049 ,20.21455059 ,19.7075258 ,15.30126158 ,11.58231258 ,32.36084773 ,26.40114966 ,17.04361386 ,21.58377595 ,27.05269037 ,17.51271274 ,16.79445259 ,23.03344324 ,20.69212554 ,21.86870081 ,19.3885395 ,17.64304802 ,20.03670675 ,21.923849 ,19.44815376 ,14.45276709 ,20.11264535 ,18.56801909 ,20.6669469 ,9.612771739 ,27.45677889 ,15.50484788 ,28.57142857 ,20.22797527 ,16.09682442 ,20.20900753 ,18.6511662 ,9.024369241 ,16.2411269 ,18.31363636 ,25.72490706 ,21.43559489 ,18.89596603 ,24.45813621 ,21.83639857 ,18.42764894 ,22.81740055 ,19.49798 ,21.78024834 ,22.14152133 ,22.30536086 ,19.40890688 ,21.26692456 ])
x3_1000=np.array([15.17555825 ,16.50677683 ,17.41893192 ,17.10980258 ,18.60593428 ,15.46355377 ,15.73685807 ,18.82155822 ,12.69766963 ,14.90826331 ,14.33769442 ,19.77244162 ,12.5142672 ,14.16880269 ,13.90023631 ,17.52164631 ,13.67193057 ,16.92069443 ,16.76608138 ,17.88548753 ,15.38461538 ,17.83948437 ,15.57563557 ,13.91404491 ,15.43713153 ,14.32262905 ,14.08335044 ,16.01790835 ,12.07146306 ,12.3254515 ,23.4443432 ,18.98184688 ,20.25435704 ,17.30031515 ,13.75430661 ,14.99566197 ,16.24753144 ,16.12873249 ,15.55336692 ,14.80967456 ,16.64172957 ,16.96947674 ,15.3221957 ,17.92069497 ,17.62907609 ,10.41856233 ,19.51061518 ,25 ,15.91962906 ,15.16066626 ,15.45033581 ,18.15821047 ,24.81270989 ,17.29087948 ,17.45151515 ,15.0929368 ,15.83087512 ,16.1358811 ,13.41181648 ,13.36810321 ,14.84837624 ,16.16815806 ,16.69646996 ,15.07363558 ,15.9222372 ,15.45747301 ,16.68825911 ,14.05222437 ])
x4_1000=np.array([14.31873923 ,16.01743425 ,14.81481481 ,19.52386973 ,16.9139284 ,15.40528042 ,13.30978528 ,15.49710191 ,6.947671969 ,16.0133508 ,14.27001478 ,15.47264669 ,12.4223544 ,13.91556777 ,13.86085109 ,13.86846163 ,14.82429933 ,12.98394327 ,13.15634714 ,14.70143613 ,12.88584027 ,15.21719936 ,15.49647035 ,14.40611422 ,20.94647784 ,12.00325088 ,12.00985424 ,14.70010229 ,12.96475133 ,12.08341091 ,14.5468975 ,16.29834254 ,12.76495525 ,14.41810565 ,16.14823443 ,17.73109584 ,15.72381124 ,15.3112938 ,14.38996782 ,14.58161413 ,14.86338073 ,13.82630814 ,19.37947494 ,14.92223623 ,24.17346014 ,6.642402184 ,11.26295553 ,7.142857143 ,16.53786708 ,15.64478837 ,15.57961882 ,14.21074573 ,14.1565487 ,14.22066938 ,16.50909091 ,11.52416357 ,14.25762045 ,14.64968153 ,11.71746067 ,14.3151249 ,15.42631514 ,12.7731018 ,16.14014173 ,14.15680046 ,13.13878137 ,13.16537223 ,15.90283401 ,14.38104449])
x5_1000=np.array([5.612548748 ,5.613783529 ,5.117306859 ,4.476816646 ,4.15644924 ,5.032090436 ,5.933527041 ,4.885540897 ,10.59537296 ,5.282222035 ,5.017797401 ,4.604088113 ,5.470130222 ,6.58565208 ,6.842953709 ,5.79112798 ,4.709062456 ,5.632080854 ,5.785656277 ,7.917611489 ,7.251347379 ,5.69044676 ,5.289985114 ,5.213840758 ,3.029107943 ,7.339487778 ,7.965510162 ,4.736489092 ,4.345726702 ,7.838391361 ,5.670027336 ,5.10767843 ,6.076307113 ,7.012658853 ,4.949341764 ,4.588426215 ,4.704855631 ,4.93317447 ,5.054562118 ,5.501958019 ,4.819851365 ,5.922965116 ,7.064439141 ,5.114193639 ,2.864583333 ,9.212920837 ,6.185222334 ,7.142857143 ,4.173106646 ,4.824234417 ,4.963776365 ,5.080721899 ,5.261345044 ,5.28164672 ,4.783333333 ,8.921933086 ,7.32546706 ,4.670912951 ,6.986467158 ,5.10568213 ,5.399580471 ,6.514574289 ,4.202265051 ,6.627201848 ,7.05432088 ,6.184883501 ,4.842105263 ,5.618955513])
x6_1000=np.array([9.673794018 ,10.49013918 ,11.63024286 ,7.949352456 ,7.926679745 ,8.085560239 ,9.016935309 ,9.848727362 ,15.25012406 ,9.353976592 ,8.452881535 ,17.88053185 ,9.930726375 ,8.748957722 ,8.850684204 ,9.239710592 ,8.550291649 ,11.14190236 ,10.34473102 ,10.81821618 ,12.00391965 ,8.904291012 ,9.664470601 ,6.983196357 ,7.852328465 ,12.67009815 ,10.61383699 ,10.7049315 ,12.65089329 ,10.38912679 ,10.81684842 ,9.04837073 ,15.12011305 ,9.572309332 ,9.286397725 ,8.04132146 ,9.331891963 ,7.999814143 ,9.53973579 ,8.988131855 ,9.555944951 ,8.521075581 ,5.298329356 ,11.06907664 ,6.884057971 ,15.57476494 ,11.39251087 ,10.71428571 ,7.670015456 ,10.1023923 ,8.669076155 ,9.710495915 ,10.26005339 ,9.113559831 ,8.63030303 ,12.34200743 ,14.25762045 ,8.067940552 ,12.33359005 ,9.813340653 ,8.505855186 ,11.24922477 ,9.411219286 ,10.0996246 ,11.20340973 ,9.954536844 ,8.995951417 ,10.71566731])

x100=np.dstack((x1_100,x2_100,x3_100,x4_100,x5_100,x6_100)).reshape(-1,num_ft)
x1000=np.dstack((x1_1000,x2_1000,x3_1000,x4_1000,x5_1000,x6_1000)).reshape(-1,num_ft)
x100test=x100[-10:]
x1000test=x1000[-10:]
x100=x100[:10]
x1000=x1000[:10]

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