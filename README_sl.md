# Flow.Launcher.Plugin.SlovenskeZeleznice

To je vtičnik za FlowLauncher, zasnovan za zagotavljanje informacij o voznem redu vlakov med postajama Poljčane in Maribor. Prikazuje čase odhoda in predvidene čase prihoda vlakov na ciljno postajo. Ta vtičnik je bil ustvarjen za mojo osebno uporabo, zato ni dodan v Flow's Plugin Store.

## Primer
![Slika zaslona](/Images/screenshot.png)

## Uporaba
Tukaj so ukazi za uporabo tega vtičnika.
| Ukaz | Primer | Opis |
| -------- | -------- | -------- |
| sz   | sz   | Prikazuje informacije o voznem redu vlakov med postajama Maribor in Poljčane.   |
| sz 1  | sz 1 | Prikazuje informacije o voznem redu vlakov med postajama Poljčane in Maribor.   |
| sz 2  | sz 2 | Prikazuje informacije o voznem redu vlakov med postajama Maribor in Poljčane.   |

## Namestitev
Obstajata dva načina namestitve vtičnika za osebno uporabo. Ker vtičnik ni dodan v Flow's Plugin Store, ga je treba namestiti ročno.

1. **Prenos datoteke zip**
   - S [GitHub-a](https://github.com/Rozman123Rok/Flow.Launcher.Plugin.SlovenskeZeleznice) prenesite zip datoteko.
   - Shrani jo v `%APPDATA%\Roaming\FlowLauncher\Plugins\` in jo nato razširi.
   - Ponovno zaženite Flow Launcher (`restart Flow Launcher`).
   - Sedaj lahko uporabljate vtičnik.

2. **Namestitev**
   - Klonirajte repozitorij v `%APPDATA%\Roaming\FlowLauncher\Plugins\`.
   - Premaknite se v mapo vtičnika in namestite odvisnosti z uporabo `pip install -r requirements.txt --target ./lib`.
   - Ponovno zaženite Flow Launcher (`restart Flow Launcher`).
   - Sedaj lahko uporabljate moj vtičnik.
