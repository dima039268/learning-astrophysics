e = 2.7182818284
print("рассчет давления на планетах")
while True:
  choise_planet = input("выберете планету : Кербин, Ева, Дюна, Джул, Лейт\n:").strip().lower()
  if choise_planet in["кербин","ева", "дюна","джул", "лейт"]:
    p_o = {"кербин":1.0, "ева":5.0,"дюна":0.067,"джул":15.0,"лейт":0.6}[choise_planet]
    h_scale = {"кербин":5600.0, "ева":7000.0,"дюна":3000.0,"джул":10000.0,"лейт":8000.0}[choise_planet]
    while True:
      height = float(input("введите высоту\n:").strip().replace(',', '.'))
      if height >+ 0:
        negative_height_to_h_scale_ratio = float(-height/h_scale)
        e_to_the_power_of_negative_ratio = float(e**negative_height_to_h_scale_ratio)
        pressure = float(p_o * e_to_the_power_of_negative_ratio)
        print(pressure)
        break
      else:
        print("высота не может быть меньше нуля,введите высоту заново")
    break
  else:
      print("вы ввели неправильное название планеты, попробуйте еще раз")

