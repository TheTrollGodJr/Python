string = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƒȘșȚțˆˇˉ˘˙˚˛˜˝ˤΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧ"
#print(len(string))

count = 0

with open("FileToText/output.txt", "w", encoding='utf-8') as f:
    f.write("numConvert = {\n")

with open("FileToText/output.txt", "a", encoding='utf-8') as f:

    for items in string:
        f.write(f"  {count}:'{items}',\n")
        count += 1
    
    f.write("}\n\n")

    count = 1
    f.write("symbolConvert = { # converts from text back into int value\n")
    
    for items in string:
        f.write(f"  '{items}':{count},\n")
        count += 1
    
    f.write("}\n\n")

    
