import json
import io
import requests
d=json.load(open('rb3.json'))



for i in d:
    try:
        if int(d[i]['Live'])>0:
            matchid=d[i]["MatchID"]

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
            skor=datas['d']['s']
            GoalTotal=int(skor[0])+int(skor[4])
            d[i]['Skor']=skor
            if live=="MS":
                d[i]['Live']=str("-2")
            else:
                d[i]['Live']=str(minut)
            say=d[i]['Bet'][0]
            au=d[i]['Bet'][4]
            print(GoalTotal,say,au)
            if au=="U":
                if GoalTotal>int(say)+0.5:
                    d[i]['Status']=1
                else:
                    d[i]['Status']=0
            if au=="A":
                if GoalTotal>int(say)+0.5:
                    d[i]['Status']=0
                else:
                    d[i]['Status']=1

    except:
        q=0
    try:
        if d[i]['Live']=="IY":
            matchid=d[i]["MatchID"]

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
            skor=datas['d']['s']
            GoalTotal=int(skor[0])+int(skor[4])
            d[i]['Skor']=skor
            d[i]['Live']=str(minut)
            say=d[i]['Bet'][0]
            au=d[i]['Bet'][4]
            if au=="U":
                if GoalTotal>int(say)+0.5:
                    d[i]['Status']=1
                else:
                    d[i]['Status']=0
            if au=="A":
                if GoalTotal>int(say)+0.5:
                    d[i]['Status']=0
                else:
                    d[i]['Status']=1
    except:
        q=1


with io.open('rb3.json', "w", encoding="utf-8") as f:
    f.write(json.dumps(d))
