import json

with open("./text_7.txt",encoding="utf8",mode="r") as src:
    src_list = [line.split() for line in src]
    
    src_dict = {firma[0]:float(firma[2])-float(firma[3]) for firma in src_list}
    out_dict = {name:value for (name,value) in src_dict.items() if value>0}
    out=[]
    out.append(out_dict)
    out.append({"average_profit":sum(out_dict.values())/len(out_dict)})
    json_out=json.dumps(out)
    print("write to file out.txt:",json_out,sep="\n")
    with open("./text_7.json",encoding="utf8",mode="w") as fout:
        fout.write(json_out)



