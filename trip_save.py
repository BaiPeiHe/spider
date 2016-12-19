
###
##  抓取保存页面 保存内容的信息
#   用 cookie 模仿登录


from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Cookie' : 'ServerPool=C; TAUnique=%1%enc%3Aw15YmyxtSRYoIfSH8Zr4w%2BXpW979EnFI4T2JuZ5ZC2AzCz8WA%2FdwMw%3D%3D; TASSK=enc%3AAHMB%2ByZOSaIls6eaE0RbbgxPIV%2F3tQYTMBrwcC19Rcb4TqVwMJTdiQIrkjfRddHPfftbpI1XW0mnqAT15EIzUU9kKvx8G51d8fmk5OAaYsUJKvAVMUIshAXXxVtJ6Yd5NA%3D%3D; _jzqy=1.1481965183.1481965183.1.jzqsr=baidu|jzqct=%E7%8C%AB%E9%80%94%E9%B9%B0.-; _smt_uid=5854fe7f.74457bc; __gads=ID=6261b3f18e975880:T=1481965183:S=ALNI_MYE9ZeoP2uNjw_sTS2jWrov7cODwQ; CommercePopunder=SuppressAll*1482062542260; VRMCID=%1%V1*id.16631*llp.%2F-a_tttype%5C.text-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.logo-m16631*e.1482667502879; bdshare_firstime=1482066418246; SecureLogin2=3.4%3AAKE6desS9tNNVJkr0m5ivA1sxiMlWRxqyLnaRWVKLXJAVUzAkPuhOyXM4Yvmc332flb0szPzFZfqo3Vu5Nl4GITR661atB9MReItD91jJclA2vlUh1KsfePzcoGB7usQasNWIi1ENjzbEWkASOef9iwVVzyt5UemY16hnYMqNvipfacuM4H3YSgs9QaOW2puoABdFiGW1BKiWzFmM84GHt4%3D; TAAuth2=%1%3%3Abc7ed7b01c00ad6833d67bef40ea57ca%3AAARSp487UlXG28c%2BPB2UCG66dvKIS%2FJivaStKXwp3fKBsOO7N5sF8IW5Vb9Grok7axPP0feuEbB%2FYbTPYG3uywPPJxgudkutTptKysILC3kCmWW1voKy58hquKv%2Bvc0xIAwTwZZN74xsj3bdolcud3M5rk%2FFfEKUmbzkAf%2FHERNsszso5LdSykH6BarzQeEBTO3DkzCioLvoJ%2FsFV%2BEJmETCBoRhEPkPBL7dHaMtLQ5x; _jzqx=1.1482066661.1482066661.1.jzqsr=tripadvisor%2Ecn|jzqct=/attraction_review-g60763-d136028-reviews-lincoln_center_for_the_performing_arts-new_york_city_new_y.-; _jzqckmp=1; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_353l136028_353l288031_353*RS.1; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CHomeASess%2C2%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Cbookstickcook%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCPers%2C%2C-1%7CCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CViatorMCSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C8%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CPremiumORPers%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cbookstickpers%2C%2C-1%7Cperssticker%2C%2C-1%7CRBAPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d288031-Reviews-Chelsea_Market-New_York_City_New_York.html; roybatty=TNI1625!AB6MfSJoqlBxHWej2Gv%2B3RA%2FqFnMOXSLKQe2D12cYEyNE5Icj18UR%2BngMW4CsxmfPCdf0milgppLO13uT%2BoCoaWdTBtOvaZSQe7wLqGnPYEETB7X2Gvs5mfrDn7H%2F%2Fks9hvKNS8Jb3TmsnDCuNaLYOiHllOr6N6Ydnmw4qphZt2Q%2C1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1481965183; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1482068040; _qzja=1.248277791.1481965183395.1481965183395.1482066661138.1482067408600.1482068040346..0.0.11.2; _qzjb=1.1482066661138.5.0.0.0; _qzjc=1; _qzjto=5.1.0; _jzqa=1.1782051137236092000.1481965183.1481965183.1482066661.2; _jzqc=1; _jzqb=1.5.10.1482066661.1; TASession=%1%V2ID.F6339A524FF7F524FC37B78DE0FCF040*SQ.88*MC.16631*LR.http%3A%2F%2Fbzclk%5C.baidu%5C.com%2Fadrc%5C.php%3Ftpl%3Dtpl_10144_14402_1%3Fl%3D1045915587%3Fie%3Dutf-8%3Ff%3D8%3Ftn%3Dbaidu%3Fwd%3D%25E7%258C%25AB%25E9%2580%2594%25E9%25B9%25B0%3Foq%3Di%2520was%2520a%2520little%2520girl%2520alone%2520in%2520my%2520little%3Frqlang%3Dcn%3FinputT%3D9701*LP.%2F-a_tttype%5C.text-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.logo-m16631*PR.427%7C*LS.ActionRecord*GR.15*TCPAR.63*TBR.17*EXEX.67*ABTR.85*PPRP.37*PHTB.92*FS.18*CPU.24*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.713EC455CBD880A43B283D7607F8A630*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.288031; TAUD=LA-1481965180454-1*LG-102861520-2.1.F.*LD-102861521-.....'
}

url_save = 'https://www.tripadvisor.cn/Saves/all'

web_data = requests.get(url_save)

soup = BeautifulSoup(web_data.text,'lxml')

titles = soup.select('div.saves-item-card card is-fullwidth')


print(titles)
print(soup)