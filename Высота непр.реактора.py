'''
Составить материальный баланс для реактора в котором осуществляестя процесс Фишера-Тропша в стационарном режиме. 
Смесь отходящих продуктов попадает в систему разделения, где выделяют твердые парафины, реакционная воды, газы, которые содержат CO2, CH4, CO, H2, 
а так же жидкие парафины, подвергаемые затем фракционированию. Мольное соотношение потоков на входе в реактор F_H2O:F_CO_0 = 2:1.
Считать, что водород и оксид углерода подаются 100%-й чистоты. Анализ отходящих поток позволяет рассчитать по формуле (11.20) селективность
S_CO_i,G  образования следующих фракций продуктов:
1) CH4 = -0,1757            4)C14H30 = - 0,4856
2) C4H10 = -0,2222          5) C36H74 = -0,2072
3) C6H14 = -0,3692          6) C3,5H7OH = -0,0273
Степень превращения оксида углерода 0,6 (X_CO = 0,6). Производительность реактора по суммарному потоку  водорода и оксида углерода равна 20кмоль/ч.
'''
#Необходимые модули
from pint import UnitRegistry
unit = UnitRegistry()

#Дано:
G_CO = 0
X_CO = 0.6
P = 20 * unit.kilomol / unit.hour
mol_frac_H2_0 = 2/3
mol_frac_CO = 1/3
M_H2 = 2 * unit.kg / unit.kilomol
M_CO = 28 * unit.kg / unit.kilomol
M_CH4 = 16 * unit.kg / unit.kilomol
M_C4H10 = 58 * unit.kg / unit.kilomol
M_C6H14 = 86 * unit.kg / unit.kilomol
M_C14H30 = 198 * unit.kg / unit.kilomol
M_C36H74 = 506 * unit.kg / unit.kilomol
M_C3_5H7OH = 66 * unit.kg / unit.kilomol
M_CO2 = 44 * unit.kg / unit.kilomol
M_H2O = 18 * unit.kg / unit.kilomol

#Решение
S_CO_CH4 = 0.1757
S_CO_C4H10 = 0.2222 
S_CO_C6H14 = 0.3692 
S_CO_C14H30 = 0.4856
S_CO_C36H74 = 0.2072
S_CO_C3_5H7OH = 0.0273
v_CH4_CO = -1
v_C4H10_CO = -4
v_C6H14_CO = -6
v_C14H30_CO = -14
v_C36H74_CO = -36
v_C3_5H7OH_CO = -3.5

print('Определим потоки CO и Н2 на входе в реактор: ')
F_H2_0 = round((P * mol_frac_H2_0), 2)
G_H2_0 = round((F_H2_0 * M_H2), 2)
F_CO_0 = round((P - F_H2_0), 2)
G_CO_0 = round((F_CO_0 * M_CO), 2)
print(f'F_H2_0 = {F_H2_0}\nG_H2_0 = {G_H2_0}\nF_CO_0 = {F_CO_0}\nG_CO_0 = {G_CO_0}\n')

print('Найдем теперь количесвта ключевых веществ (фракций), образующихся в реакторе. Согласно (11.19) и (11.22) имеем (кг/ч): ')
G_CH4 = round(-G_CO_0*X_CO*S_CO_CH4/v_CH4_CO, 2)
G_C4H10 = round(-G_CO_0*X_CO*S_CO_C4H10/v_C4H10_CO, 2)
G_C6H14 = round(-G_CO_0*X_CO*S_CO_C6H14/v_C6H14_CO, 2)
G_C14H30 = round(-G_CO_0*X_CO*S_CO_C14H30/v_C14H30_CO, 2)
G_C36H74 = round(-G_CO_0*X_CO*S_CO_C36H74/v_C36H74_CO, 2)
G_C3_5H7OH = round(-G_CO_0*X_CO*S_CO_C3_5H7OH/v_C3_5H7OH_CO, 2)
print(f'G_CH4 = {G_CH4}\nG_C4H10 = {G_C4H10}\nG_C6H14 = {G_C6H14}\nG_C14H30 = {G_C14H30}\nG_C36H74 = {G_C36H74}\nG_C3_5H7OH = {G_C3_5H7OH}\n')

print('Определим количество непрореагировашего оксида углерода: ')
G_CO = round(G_CO_0*(1-X_CO), 2)
d_G_CO = round(G_CO - G_CO_0, 2)
print(f'G_CO = {G_CO}\nd_G_CO = {d_G_CO}\n')

print('Запишем уравнения мольного баланса для процесса Фишера-Тропша по схеме суммарных реакций (11.22).\nВводя химические переменные стадий и затем исключая их, окончательно получим: ')
print('d_N_CO  = - d_N_CH4 - 4*d_N_C4H10 - 6*d_N_C6H14 - 14*d_N_C14H30 - 36*d_N_C36H74 - 3.5*d_NC3_5H7OH - d_N_CO2')
print('d_N_H2 = - 3*d_N_CH4 - 9*d_N_C4H10 - 13*d_N_C6H14 - 29*d_N_C14H30 - 73*d_N_C36H74 - 6.5*d_NC3_5H7OH - d_N_CO2')
print('d_N_H2O = - d_N_CH4 - 4*d_N_C4H10 - 6*d_N_C6H14 - 14*d_N_C14H30 - 36*d_N_C36H74 - 2.5*d_NC3_5H7OH - d_N_CO2\n')

print('Уравнения массового баланса имеют вид (N_i = G_i/C_i): ')
print('d_G_CO = -(M_CO/M_CH4) * d_G_CH4 -4 *(M_CO/M_C4H10) * d_G_C4H10 -6 * (M_CO/M_C6H14) * d_G_C6H14 -14 *(M_CO/M_C14H30) * d_G_C14H30 - 36 * (M_CO/M_C36H74) * d_G_C36H74 -3.5 *(M_CO/M_C3_5H7OH) * d_G_C3_5H7OH - (M_CO/M_CO2) * d_G_CO2 = -1.75*d_G_CH4 - 1.931*d_G_C4H10 - 1.953*d_G_C6H14 - 1.980*d_G_C14H30 - 1.992*d_G_C36H74 - 1.485*d_G_C3_5H7OH - 0.636*d_G_CO2') 
print('d_G_H2 = - 0.375 * d_G_CH4 - 0.310 * d_G_C4H10 - 0.300* d_G_C6H14 - 0.290* d_G_C14H30 - 0.290 * d_G_C36H74 - 0.197 * d_G_C3_5H7OH + 0.045 * d_G_CO2')
print('d_G_H2O = 1.125 * d_G_CH4 + 1.240 * d_G_C4H10 + 1.260 * d_G_C6H14 + 1.270 * d_G_C14H30 + 0.682 * d_G_C3_5H7OH - 0.410 * d_G_CO2 + 1.280 * d_G_C36H74\n')

print('Из первого уравнения массового баланса процесса Фишера-Тропша найдем d_G_CO2:')
G_CO2 = round((v_CH4_CO * (M_CO/M_CH4)*G_CH4 + v_C4H10_CO *(M_CO/M_C4H10)*G_C4H10 + v_C6H14_CO * (M_CO/M_C6H14)*G_C6H14 + v_C14H30_CO* (M_CO/M_C14H30)*G_C14H30 + v_C36H74_CO * (M_CO/M_C36H74)*G_C36H74 + v_C3_5H7OH_CO * (M_CO/M_C3_5H7OH)*G_C3_5H7OH - d_G_CO) /(M_CO/M_CO2), 2)
print(f'd_G_CO2 = {G_CO2}\n')

print('Из второго уравнения определим массовые потоки d_G_H2 и G_H2: ')
d_G_H2 = round(- 0.375 * G_CH4 - 0.310 * G_C4H10 - 0.300* G_C6H14 - 0.290* G_C14H30 - 0.290 * G_C36H74 - 0.197 * G_C3_5H7OH + 0.045 * G_CO2, 2)
G_H2 = round(G_H2_0 + d_G_H2, 2)
print(f'G_H2 = G_H2_0 + d_G_H2 = {G_H2}\n')

print('Из третьего уравнения найдем d_G_H2O: ')
G_H2O = round(((-1)*v_CH4_CO * (M_H2O/M_CH4)*G_CH4 + (-1)*v_C4H10_CO *(M_H2O/M_C4H10)*G_C4H10 + (-1)*v_C6H14_CO * (M_H2O/M_C6H14)*G_C6H14 + (-1)*v_C14H30_CO* (M_H2O/M_C14H30)*G_C14H30  + (-1)*v_C3_5H7OH_CO * (M_H2O/M_C3_5H7OH)*G_C3_5H7OH - (M_H2O/M_CO2) * G_CO2+ (-1)*v_C36H74_CO * (M_H2O/M_C36H74)*G_C36H74), 2)
print(f'G_H2O = {G_H2O}\n')

s_arrival = round(G_H2_0 + G_CO_0, 2)
s_consumption = round(G_C3_5H7OH + G_CH4 + G_C4H10 + G_C6H14 + G_C14H30 + G_C36H74 + G_CO2 + G_H2O + G_H2 + G_CO, 2)

print(f'Приход G_H2_0 = {G_H2_0}, G_CO_0 = {G_CO_0}\nРасход G_C3_5H7OH = {G_C3_5H7OH}, G_CH4 = {G_CH4}, G_C6H14 = {G_C6H14}, G_C14H30 = {G_C14H30}, G_C36H74 = {G_C36H74}, G_CO2 = {G_CO2}, G_H2O = {G_H2O}, G_H2 = {G_H2}, G_CO = {G_CO}\n')
print(f'Суммарный приход = {s_arrival}\nСуммарный расход = {s_consumption}')