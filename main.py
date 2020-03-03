import pandas as pd
import requests
import numpy as np
import math
import io
import json
#Belarus, Bra2, Cezayir, Ekvator, Endonezya, Güney Kore, İrlanda, İsveç2, Katar, Letonya, singapur, Uruguay, Çin
urls=(['Arj','54915']
     ,['Arj2','55157']
     ,['Avus','54765']
     ,['Avus2','54764']
     ,['Avus3','55242']
     ,['Avus4','55239']
     ,['Avustrl','55287']
     ,['Aze','55118']
     ,['BAE','54847']
     ,['Belc','54830']
#     ,['Bra','53378']
     ,['Isvcre','54751']
     ,['Isvcre2','54781']
     ,['Alm','54798']
     ,['Alm2','54799']
     ,['Alm3','54836']
     ,['Dan','54581']
     ,['Dan2','54759']
     ,['Dan3','55035']
     ,['Dan4','55036']
     ,['Ing','54669']
     ,['Ing2','54755']
     ,['Ing3','54756']
     ,['Ing4','54757']
     ,['Ing5','54841']
     ,['Isp','54839']
     ,['Isp2','54844']
     ,['Fr','54705']
     ,['Fr2','54723']
     ,['Fr3','54933']
     ,['GAf','54866']
     ,['Hir','54682']
     ,['Hol','54721']
     ,['Ita','55017']
     ,['Ita2','55235']
     ,['Ita3','55294']
     ,['Ita4','55295']
     ,['Ita5','55296']
     ,['Jap','53310']
     ,['Mac','54870']
     ,['Nor','56318']
     ,['Pol','54562']
     ,['Pol2','54783']
     ,['Pol3','54784']
     ,['Port','54873']
     ,['Port2','54874']
     ,['Para','56313']
     ,['Rom','54829']
     ,['Rus','54579']
     ,['Rus2','54640']
     ,['Slvk','54738']
     ,['Slvn','54786']
     ,['Sudi','55213']
     ,['Isk','54763']
     ,['Isk2','54760']
     ,['Isk3','54761']
     ,['Isk4','54762']
     ,['Isvc','53136']
     ,['Tun','55293']
     ,['Tr','54794']
     ,['Tr2','54902']
     ,['Tr3','54897']
     ,['Tr4','54898']
     ,['Tr5','54899']
     ,['Ukr','54672']
     ,['YZel','55773']
     ,['Yun','54837']
     ,['Misir','55612']
     ,['Fas','55332']
     ,['Galler','54801'])
expo=float(np.exp(1))
Out=pd.DataFrame(columns=['MatchID','BetID','League','Hafta','Home','Away','Gun','Saat','Bet','Prob','Odds'])
jsonfile=json.load(open('db.json'))
for leag in range(len(urls)):
    lig=urls[leag][0]
    print(lig,leag)
    try:

        url = 'http://arsiv.mackolik.com/AjaxHandlers/StandingHandler.ashx'
        params = {
            'op': 'standing',
            'id': urls[leag][1],
        }
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Host': 'arsiv.mackolik.com',
                   'Referer': 'http://arsiv.mackolik.com/Puan-Durumu'}

        response = requests.get(url, params=params, headers=headers)

        data = response.json()
        homeaway=pd.DataFrame(columns=['id','Play','Ou','AtEv','YeEv','AtDe','YeDe'])
        TeamCode={}
        for i in range(len(data['s'])):
            team=data['s'][i]
            TeamCode[team[0]]=team[1]
            homeaway=homeaway.append({'id':team[0],'Play':team[2],'Ou':team[3],'AtEv':team[10],'YeEv':team[12],'AtDe':team[11],'YeDe':team[13]},ignore_index=True)
        GamePlayed=homeaway['Play'].sum()
        hafta=homeaway['Play'].mean()+homeaway['Ou'].mean()
        hafta=int(hafta)
        IcerdeAtilanToplamGol=homeaway['AtEv'].sum()
        IcerdeYenilenToplamGol=homeaway['YeEv'].sum()
        EvSahibiGolAtmaOrt=IcerdeAtilanToplamGol/GamePlayed
        DepsGolYemeOrt=EvSahibiGolAtmaOrt
        EvSahibiGolYemeOrt=IcerdeYenilenToplamGol/GamePlayed
        DepsGolAtmaOrt=EvSahibiGolYemeOrt
        homeaway['HucEv']=homeaway['AtEv']/homeaway['Play']/EvSahibiGolAtmaOrt
        homeaway['SavEv']=homeaway['YeEv']/homeaway['Play']/EvSahibiGolYemeOrt
        homeaway['HucDep']=homeaway['AtDe']/homeaway['Ou']/DepsGolAtmaOrt
        homeaway['SavDep']=homeaway['YeDe']/homeaway['Ou']/DepsGolYemeOrt
        for i in range(len(data['f'])):
            match=data['f'][i]
            id=match[0]
            gun=match[1]
            if int(gun[3:])==12:
                gun=gun+'/2019'
            else:
                gun=gun+'/2020'
            saat=match[2]
            ev=match[3]
            dep=match[4]
            HucAdj=float(homeaway[homeaway['id']==ev]['HucEv'])*float(homeaway[homeaway['id']==dep]['SavDep'])*EvSahibiGolAtmaOrt
            SavAdj=float(homeaway[homeaway['id']==ev]['SavEv'])*float(homeaway[homeaway['id']==dep]['HucDep'])*EvSahibiGolYemeOrt
            ss=HucAdj**0*expo**-HucAdj/math.factorial(0)*SavAdj**0*expo**-SavAdj/math.factorial(0)
            bs=HucAdj**1*expo**-HucAdj/math.factorial(1)*SavAdj**0*expo**-SavAdj/math.factorial(0)
            sb=HucAdj**0*expo**-HucAdj/math.factorial(0)*SavAdj**1*expo**-SavAdj/math.factorial(1)
            bb=HucAdj**1*expo**-HucAdj/math.factorial(1)*SavAdj**1*expo**-SavAdj/math.factorial(1)
            iis=HucAdj**2*expo**-HucAdj/math.factorial(2)*SavAdj**0*expo**-SavAdj/math.factorial(0)
            si=HucAdj**0*expo**-HucAdj/math.factorial(0)*SavAdj**2*expo**-SavAdj/math.factorial(2)
            ib=HucAdj**2*expo**-HucAdj/math.factorial(2)*SavAdj**1*expo**-SavAdj/math.factorial(1)
            bi=HucAdj**1*expo**-HucAdj/math.factorial(1)*SavAdj**2*expo**-SavAdj/math.factorial(2)
            us=HucAdj**3*expo**-HucAdj/math.factorial(3)*SavAdj**0*expo**-SavAdj/math.factorial(0)
            su=HucAdj**0*expo**-HucAdj/math.factorial(0)*SavAdj**3*expo**-SavAdj/math.factorial(3)


            url=('http://arsiv.mackolik.com/AjaxHandlers/IddaaHandler.aspx')
            params = {
                'command': 'morebets',
                'mac': id,
                'type':'ByLeague',
            }
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                       'X-Requested-With': 'XMLHttpRequest',
                       'Host': 'arsiv.mackolik.com',
                       'Referer': 'http://arsiv.mackolik.com/Iddaa-Programi'}

            response = requests.get(url, params=params, headers=headers)
            out=response.text

            a=out.find('SOV":1.5')
            b=out.find('SOV":1.5',a+10)
            c=out.find("Odd",b+10)
            balt=out[c+5:c+9]
            balt=balt.replace("}","0")
            out[c+5:]
            d=out.find("Odd",c+10)
            bust=out[d+5:d+9]
            bust=bust.replace("}","0")

            a=out.find('SOV":2.5')
            b=out.find('SOV":2.5',a+10)
            c=out.find("Odd",b+10)
            ialt=out[c+5:c+9]
            ialt=ialt.replace("}","0")
            out[c+5:]
            d=out.find("Odd",c+10)
            iust=out[d+5:d+9]
            iust=iust.replace("}","0")

            a=out.find('SOV":3.5')
            b=out.find('SOV":3.5',a+10)
            c=out.find("Odd",b+10)
            ualt=out[c+5:c+9]
            ualt=ualt.replace("}","0")
            out[c+5:]
            d=out.find("Odd",c+10)
            uust=out[d+5:d+9]
            uust=uust.replace("}","0")

            a=out.find('"Title":"Toplam Gol","Name":"0,5 Alt/Üst"')
            b=out.find('MarketNo',a+10)
            bid=out[b+10:b+15].replace(",","")

            a=out.find('"Title":"Toplam Gol","Name":"1,5 Alt/Üst"')
            b=out.find('MarketNo',a+10)
            iid=out[b+10:b+15].replace(",","")

            a=out.find('"Title":"Toplam Gol","Name":"2,5 Alt/Üst"')
            b=out.find('MarketNo',a+10)
            uid=out[b+10:b+15].replace(",","")

            print(id,TeamCode[ev],TeamCode[dep],gun,saat,'1.5alt:',balt,'1.5ust:',bust,'2.5alt',ialt,'2.5ust',iust,'3.5alt',ualt,'3.5ust',uust)


            bet='1,5 Alt'
            pr=ss+bs+sb
            Out=Out.append({'MatchID':id,'BetID':bid,'League':lig,'Hafta':hafta,'Home':TeamCode[ev],'Away':TeamCode[dep],'Gun':gun,'Saat':saat,'Bet':bet,'Prob':pr,'Odds':balt},ignore_index=True)

            bet='1,5 Ust'
            pr=1-pr
            Out=Out.append({'MatchID':id,'BetID':bid,'League':lig,'Hafta':hafta,'Home':TeamCode[ev],'Away':TeamCode[dep],'Gun':gun,'Saat':saat,'Bet':bet,'Prob':pr,'Odds':bust},ignore_index=True)

            bet='2,5 Alt'
            pr=ss+bs+sb+iis+si+bb
            Out=Out.append({'MatchID':id,'BetID':iid,'League':lig,'Hafta':hafta,'Home':TeamCode[ev],'Away':TeamCode[dep],'Gun':gun,'Saat':saat,'Bet':bet,'Prob':pr,'Odds':ialt},ignore_index=True)

            bet='2,5 Ust'
            pr=1-pr
            Out=Out.append({'MatchID':id,'BetID':iid,'League':lig,'Hafta':hafta,'Home':TeamCode[ev],'Away':TeamCode[dep],'Gun':gun,'Saat':saat,'Bet':bet,'Prob':pr,'Odds':iust},ignore_index=True)

            bet='3,5 Alt'
            pr=ss+bs+sb+iis+si+bb+bi+ib+us+su
            Out=Out.append({'MatchID':id,'BetID':uid,'League':lig,'Hafta':hafta,'Home':TeamCode[ev],'Away':TeamCode[dep],'Gun':gun,'Saat':saat,'Bet':bet,'Prob':pr,'Odds':ualt},ignore_index=True)

            bet='3,5 Ust'
            pr=1-pr
            Out=Out.append({'MatchID':id,'BetID':uid,'League':lig,'Hafta':hafta,'Home':TeamCode[ev],'Away':TeamCode[dep],'Gun':gun,'Saat':saat,'Bet':bet,'Prob':pr,'Odds':uust},ignore_index=True)

        for d in data['r']:
            matchid=d[0]
            minute=d[2]
            if minute=="MS":
                live=str(-2)
            elif minute=="Ert.":
                live=str(-2)
            else:
                try:
                    url = 'http://arsiv.mackolik.com/Match/MatchData.aspx'
                    params = {
                        't': 'dtl',
                        'id': matchid,
                        's':'0',
                    }
                    headers = {
                               'Referer': 'http://arsiv.mackolik.com/Puan-Durumu'}

                    responses = requests.get(url, params=params, headers=headers)

                    datas = responses.json()
                    minut=datas['d']['st']

                    live=str(minut)
                except:
                    live=str(-2)
            eg=d[6]
            dg=d[7]
            skor=str(eg)+' - '+str(dg)
            gs=eg+dg
            if gs>1.5:
                try:
                    jsonfile[str(matchid)+'1,5 Ust']['Skor']=skor
                    jsonfile[str(matchid)+'1,5 Ust']['Status']=1
                    jsonfile[str(matchid)+'1,5 Ust']['Live']=live
                    print('MatchScore added successfully',matchid,skor)
                except:
                    print('No Match Record Found')
                try:
                    jsonfile[str(matchid)+'1,5 Alt']['Skor']=skor
                    jsonfile[str(matchid)+'1,5 Alt']['Status']=0
                    jsonfile[str(matchid)+'1,5 Alt']['Live']=live
                    print('MatchScore added successfully',matchid,skor)
                except:
                    print('No Match Record Found')
            else:
                try:
                    jsonfile[str(matchid)+'1,5 Ust']['Skor']=skor
                    jsonfile[str(matchid)+'1,5 Ust']['Status']=0
                    jsonfile[str(matchid)+'1,5 Ust']['Live']=live
                    print('MatchScore added successfully',matchid,skor)
                except:
                    print('No Match Record Found')

                try:
                    jsonfile[str(matchid)+'1,5 Alt']['Skor']=skor
                    jsonfile[str(matchid)+'1,5 Alt']['Status']=1
                    jsonfile[str(matchid)+'1,5 Alt']['Live']=live
                    print('MatchScore added successfully',matchid,skor)
                except:
                    print('No Match Record Found')

            if gs>2.5:
                try:
                    jsonfile[str(matchid)+'2,5 Ust']['Skor']=skor
                    jsonfile[str(matchid)+'2,5 Ust']['Status']=1
                    jsonfile[str(matchid)+'2,5 Ust']['Live']=live
                    print('MatchScore added successfully',matchid,skor)
                except:
                    print('No Match Record Found')
                try:
                    jsonfile[str(matchid)+'2,5 Alt']['Skor']=skor
                    jsonfile[str(matchid)+'2,5 Alt']['Status']=0
                    jsonfile[str(matchid)+'2,5 Alt']['Live']=live
                    print('MatchScore added successfully',matchid,skor)
                except:
                    print('No Match Record Found')
            else:
                try:
                    jsonfile[str(matchid)+'2,5 Ust']['Skor']=skor
                    jsonfile[str(matchid)+'2,5 Ust']['Status']=0
                    jsonfile[str(matchid)+'2,5 Ust']['Live']=live
                    print('MatchScore added successfully',matchid,skor)
                except:
                    print('No Match Record Found')
                try:
                    jsonfile[str(matchid)+'2,5 Alt']['Skor']=skor
                    jsonfile[str(matchid)+'2,5 Alt']['Status']=1
                    jsonfile[str(matchid)+'2,5 Alt']['Live']=live
                    print('MatchScore added successfully',matchid,skor)
                except:
                    print('No Match Record Found')
            if gs>3.5:
                try:
                    jsonfile[str(matchid)+'3,5 Ust']['Skor']=skor
                    jsonfile[str(matchid)+'3,5 Ust']['Status']=1
                    jsonfile[str(matchid)+'3,5 Ust']['Live']=live
                    print('MatchScore added successfully',matchid,skor)
                except:
                    print('No Match Record Found')
                try:
                    jsonfile[str(matchid)+'3,5 Alt']['Skor']=skor
                    jsonfile[str(matchid)+'3,5 Alt']['Status']=0
                    jsonfile[str(matchid)+'3,5 Alt']['Live']=live
                    print('MatchScore added successfully',matchid,skor)
                except:
                    print('No Match Record Found')
            else:
                try:
                    jsonfile[str(matchid)+'3,5 Ust']['Skor']=skor
                    jsonfile[str(matchid)+'3,5 Ust']['Status']=0
                    jsonfile[str(matchid)+'3,5 Ust']['Live']=live
                    print('MatchScore added successfully',matchid,skor)
                except:
                    print('No Match Record Found')
                try:
                    jsonfile[str(matchid)+'3,5 Alt']['Skor']=skor
                    jsonfile[str(matchid)+'3,5 Alt']['Status']=1
                    jsonfile[str(matchid)+'3,5 Alt']['Live']=live
                    print('MatchScore added successfully',matchid,skor)
                except:
                    print('No Match Record Found')
    except:
        print('LigdeYeterliVeriYok')





print("Mac-Oran eslesmesi bitti")
Out['Odds']=pd.to_numeric(Out['Odds'], errors='coerce').fillna(0)
indexNames = Out[ (Out['Prob'] < 0.80)].index
Out.drop(indexNames , inplace=True)
indexNames=Out[(Out['Odds']<=1)].index
Out.drop(indexNames,inplace=True)
print("Ihtimali %80 nin altındaki bahisler silindi")

print("Maclar database e aktarilmaya baslaniyor")



for i in Out.index:

    try:
        jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["League"]=Out['League'][i]
        jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["BetID"]=Out['BetID'][i]
        jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Hafta"]=Out['Hafta'][i]
        jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Home"]=Out['Home'][i]
        jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Away"]=Out['Away'][i]
        jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Gun"]=Out['Gun'][i]
        jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Saat"]=Out['Saat'][i]
        jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Prob"]=Out['Prob'][i]
        jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Odds"]=Out['Odds'][i]
        jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]['Live']=str(-1)
    except:
        try:
            jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]={}
            jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["League"]=Out['League'][i]
            jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["BetID"]=Out['BetID'][i]
            jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Hafta"]=Out['Hafta'][i]
            jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Home"]=Out['Home'][i]
            jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Away"]=Out['Away'][i]
            jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Gun"]=Out['Gun'][i]
            jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Saat"]=Out['Saat'][i]
            jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Prob"]=Out['Prob'][i]
            jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]["Odds"]=Out['Odds'][i]
            jsonfile[str(Out['MatchID'][i])+str(Out['Bet'][i])]['Live']=str(-1)
        except:
            print('DataBaseError')


with io.open('db.json', "w", encoding="utf-8") as f:
    f.write(json.dumps(jsonfile))



d=json.load(open('db.json'))

out={}
ind=0
key='Live'
for i in d:
    if key in d[i].keys():
        if d[i]['League'] not in ['Ing3','Belc','Belg'] and float(d[i]['Prob'])>0.82 and float(d[i]['Odds'])<1.58:
            out[ind]=d[i]
            l=len(i)

            out[ind]["Bet"]=i[l-7:]
            out[ind]["MatchID"]=i[:l-7]
            ind=ind+1
with io.open('rb3.json', "w", encoding="utf-8") as f:
    f.write(json.dumps(out))
