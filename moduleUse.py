#모듈을 임포트하여 사용하여보자
import module
module.price(3)
module.MorningPrice(4)
module.SoldierPrice(6)

import module as md #이런식으로 임포트시 변수처럼 만들어서 사용 가능하다.

md.SoldierPrice(1)
md.price(2)
md.MorningPrice(7)

from module import * #모두 가져다쓴다고 선언하면 변수. 할 필요없이 그냥 사용이 가능하다
price(1)
SoldierPrice(3)
MorningPrice(2)

from module import price, MorningPrice #이런식으로 필요한부분만 부분 임포트하여 사용할 수도 있다. 근데 굳이
price(2)
MorningPrice(8)

