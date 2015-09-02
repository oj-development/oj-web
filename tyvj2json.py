import json,os
def decoder(x):
    try:
        return x.decode("utf-8")
    except Exception as e:
        try:
            return x.decode("gb2312")
        except Exception as e:
            return x.decode("gbk")
def main():
    with open('config.ini', 'r') as f:
        config=f.readlines()
    num=int(config[0])
    config2=list(map(lambda x:x.split("|"),config[1:num+1]))
    export=[]
    for i in config2:
        with open(os.path.join('Input',i[0]), 'rb') as f:
            input_content=decoder(f.read())
        with open(os.path.join('Output',i[1]), 'rb') as f:
            output_content=decoder(f.read())
        export.append([input_content,output_content,int(i[3]),float(i[2]),262144])
    with open("export.json", 'w') as f:
        f.write(json.dumps(export))
if __name__ == '__main__':
    main()