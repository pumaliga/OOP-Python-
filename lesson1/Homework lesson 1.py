class Element():
    t_freezing = ''
    t_melting = ''
    t_evaporation = ''

    def agg_state(self, t):
        C = t
        F = (t * 9 / 5) + 32
        K = t + 273.15
        print("Температура в °C = {}, °F = {}, °К = {} ".format(C, F, K))
        if t >= self.t_evaporation:
            return 'Испарение'
        if t >= self.t_melting:
            return 'Плавление'
        elif t < self.t_freezing:
            return 'Затвердение'

    def conversion(self, t):
        print("Из какой шкалы конвертируем C, F, K?")
        iz = input().upper()
        print("В какую шкалу конвертировать C, F, K? ")
        v = input().upper()
        if iz == "C" and v == "F":
            return (t * 9/5) + 32
        elif iz == "C" and v == "K":
            return t + 273.15
        elif iz == "F" and v == "C":
            return 5 / 9 * (t - 32)
        elif iz == "F" and v == "K":
            return (t + 459.67) * 5/9
        elif iz == "K" and v == "C":
            return t + 273.15
        elif iz == "F" and v == "F":
            return (t + 459.67) * 5/9
        else:
            print("Неверный ввод")


class Iron(Element):
    t_melting = 1538
    t_evaporation = 2862
    t_freezing = 1538
Iron = Iron()
print(Iron.agg_state(1000))




