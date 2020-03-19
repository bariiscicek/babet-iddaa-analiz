### Bet Prediction System

[Babet](babet.metu.fun) predicts occurance probabilities of bets that are legal in Turkey.

##### How Does It Works

For every given soccer league, the system needs a **score table** that includes *goal for*, *goal against* and *matches played* values for both home and away information.

- Data of league statistics is retrieved from [MaçKolik](arsiv.mackolik.com)
- For every competition, adjusted power of teams are calculated. With different competitions, every team gets different power. The power of a team is actually goal scoring power of a team.
- Power of a team is calculated with combination of attack power of the team and defense power of opposite team.

Let's say ***Team A*** and ***Team B*** is going to have a competition.
- Power of Team A is calculated as $$P_A$$
- Power of Team B is calculated as $$P_B$$

Goal scoring probabilities are calculated for both teams using **Poisson Distribution**

Let's say, $$P(G_A=n)$$ refers to probability of team A to score n goals

$$P(G_A=n)=\frac{e^{-P_A}*P_A^n}{n!}$$

$$P(G_B=n)=\frac{e^{-P_B}*P_B^n}{n!}$$

All possible match score probabilities are calculated. 

Let's say probability of having ending match score as x-y is $$P(S=x.y)$$

For example:
probability of having **0-0** score at the end of the match is 
- $$P(S=0.0)=P(G_A=0)*P(G_B=0)$$

After all possible ending scores are calculated, Bet prediction process is started.
$$P(b)$$ refers to probability of bet ***'b'*** will occur and calculated as follows

Examples:
- $$P(1,5A)=P(S=0.0)+P(S=1.0)+P(S=0.1)$$
- $$P(1,5U)=1-P(1,5A)$$
- $$P(2,5A)=P(S=0.0)+P(S=1.0)+P(S=0.1)+P(S=2.0)+P(S=0.2)+P(S=1.1)$$
- $$P(2,5U)=1-P(2,5A)$$

Now we have prediction of all bets we define. In order to run the program your own, you need a server in order to display live scores and to check new probabilities. 

In the terminal of server, we should type:
`$ sudo nano /etc/crontab`
and then, we should insert two lines into it.

```console
*/15 * * * * root python3 /var/main.py
* * * * * root python3 /var/canli.py
```
[![!](https://images.daznservices.com/di/library/mackolik/dc/6/mackolik-logo_8mlnjr7sh2qo1txrvyog5bbtj.png?t=-1700003935&quality=70&w=1280)](arsiv.mackolik.com)
