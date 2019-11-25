from entity_extractor import *
from search_answer import *

tag = {"Disease":"疾病", "HAS_DRUG":"药品","HAS_COMPLICATION":"并发症","DEPARTMENT_IS":"科室","PART_IS":"发病部位","HAS_SYMPTOM":"症状","ALIAS_IS":"别名"}
tag1 = {"药品":6, "并发症":5, "科室":4, "发病部位":3, "症状":2, "别名":1, "疾病":0}

def get_json_data(data, label):
    json_data = {'data': [], "links": []}
    name_dict = {}
    allgroup = []

    for i in data:
        value = str(i['r']).replace(' ','')
        # print(value)
        s = re.findall(r'[(](.*?)[)]-[[]:(.*?)[{].*?[}].*?[(](.*?)[)]', value, re.S)
        for j in s:
            m = list(j)
            allgroup.append(m)

    count = 0
    for m in allgroup:
        # print(m)
        data_item = {}
        if m[0] not in name_dict:
            name_dict[m[0]] = count
            data_item['name'] = m[0]
            data_item['category'] = tag1[tag[label]]
            count += 1
            json_data['data'].append(data_item)
        data_item = {}
        if m[2] not in name_dict:
            name_dict[m[2]] = count
            data_item['name'] = m[2]
            data_item['category'] = tag1[tag[m[1]]]
            count += 1
            json_data['data'].append(data_item)

    for n in allgroup:
        # print(n[1])
        link_item = {}
        link_item['source'] = name_dict[n[0]]
        link_item['target'] = name_dict[n[2]]
        link_item['value'] = tag[n[1]]
        json_data['links'].append(link_item)

    # print(json_data)
    return json_data

def get_KGQA_answer_text(input_str):
    answer = "对不起，我没理解你的意思，你换种方式提问我，说不定我就能回答了~(@^_^@)~，如：高血压的症状有哪些？"
    entities = EntityExtractor().extractor(input_str)
    if not entities:
        return answer
    sqls = AnswerSearching().question_parser(entities)
    final_answer = AnswerSearching().searching(sqls)
    if not final_answer:
        return answer
    else:
        return '\n'.join(final_answer)

def get_KGQA_answer_graph(question):
    e = EntityExtractor()
    s = AnswerSearching()
    entities = e.extractor(question)
    sql,label = s.question_parser_graph(entities)
    res = s.searching_graph(sql)
    print(res)
    data = list(res)
    # print(data)
    json_data = get_json_data(data, label)
    return json_data


if __name__ == "__main__":
    data = get_KGQA_answer_graph("近视眼")
    print(data)



