from smartphone import Smartphone
catalog = [
    Smartphone('<Honor>',  '<x8>', '<+895 152 3636>.'),
    Smartphone('<Rusphon>', '<n42>', '<+904 154 7878>.'),
    Smartphone('<Samsung>', '<A5>', '<+926 144 2525>.'),
    Smartphone('<Apple>', '<iPhone 12>', '<+7911 251 6452>.'),
    Smartphone('<Xiaomi>', '<Redmi Note 10>', '<+795 555 6666>.')
]

for smartphone in catalog:
    print(f'{smartphone.marka} - {smartphone.model}. {smartphone.number}')
