from django.shortcuts import render, HttpResponse
import json


# Create your views here.
def index(request):
    return render(request, 'index.html')


def json_data(request):
    # print(request.POST)
    info_dict = {
        "beijing":{
            "name":"北京市",
            "type": "市辖区",
            "child": {
                "110101": "东城区",
                "110102": "西城区",
                "110105": "朝阳区",
                "110106": "丰台区",
                "110107": "石景山区",
                "110108": "海淀区",
                "110109": "门头沟区",
                "110111": "房山区",
                "110112": "通州区",
                "110113": "顺义区",
                "110114": "昌平区",
                "110115": "大兴区",
                "110116": "怀柔区",
                "110117": "平谷区",
                "110118": "密云区",
                "110119": "延庆区"
            }
        },
        "shijiazhuang": {
            "name": "石家庄市",
            "type": "市辖区",
            "child": {
                    "130101": "市辖区",
                    "130102": "长安区",
                    "130104": "桥西区",
                    "130105": "新华区",
                    "130107": "井陉矿区",
                    "130108": "裕华区",
                    "130109": "藁城区",
                    "130110": "鹿泉区",
                    "130111": "栾城区",
                    "130121": "井陉县",
                    "130123": "正定县",
                    "130125": "行唐县",
                    "130126": "灵寿县",
                    "130127": "高邑县",
                    "130128": "深泽县",
                    "130129": "赞皇县",
                    "130130": "无极县",
                    "130131": "平山县",
                    "130132": "元氏县",
                    "130133": "赵县",
                    "130183": "晋州市",
                    "130184": "新乐市"
                }
        },
        "tianjing": {
            "name": "天津市",
            "type": "市辖区",
            "child": {
                    "120101": "和平区",
                    "120102": "河东区",
                    "120103": "河西区",
                    "120104": "南开区",
                    "120105": "河北区",
                    "120106": "红桥区",
                    "120110": "东丽区",
                    "120111": "西青区",
                    "120112": "津南区",
                    "120113": "北辰区",
                    "120114": "武清区",
                    "120115": "宝坻区",
                    "120116": "滨海新区",
                    "120117": "宁河区",
                    "120118": "静海区",
                    "120119": "蓟州区"
            }
        },
        "k8s":{
    "kind": "EndpointsList",
    "apiVersion": "v1",
    "metadata": {
        "selfLink": "/api/v1/namespaces/default/endpoints",
        "resourceVersion": "9715086"
    },
    "items": [{
        "metadata": {
            "name": "voucher-center-master",
            "namespace": "default",
            "selfLink": "/api/v1/namespaces/default/endpoints/voucher-center-master",
            "uid": "8fd980bf-0507-11e9-a3b3-005056bb4630",
            "resourceVersion": "9051672",
            "creationTimestamp": "2018-12-21T10:02:44Z"
        },
        "subsets": [
            {
                "addresses": [
                    {
                        "ip": "192.169.167.105",
                        "nodeName": "job-node149",
                        "targetRef": {
                            "kind": "Pod",
                            "namespace": "default",
                            "name": "voucher-center-rc-p20kk",
                            "uid": "76dd6355-1269-11e9-95a3-005056bb4630",
                            "resourceVersion": "9051584"
                        }
                    },
                    {
                        "ip": "192.169.183.26",
                        "nodeName": "job-node137",
                        "targetRef": {
                            "kind": "Pod",
                            "namespace": "default",
                            "name": "voucher-center-rc-vknkt",
                            "uid": "7751e013-1269-11e9-95a3-005056bb4630",
                            "resourceVersion": "9051604"
                        }
                    },
                    {
                        "ip": "192.169.242.29",
                        "nodeName": "job-node145",
                        "targetRef": {
                            "kind": "Pod",
                            "namespace": "default",
                            "name": "voucher-center-rc-0x482",
                            "uid": "7790169d-1269-11e9-95a3-005056bb4630",
                            "resourceVersion": "9051627"
                        }
                    },
                    {
                        "ip": "192.169.76.159",
                        "nodeName": "job-node151",
                        "targetRef": {
                            "kind": "Pod",
                            "namespace": "default",
                            "name": "voucher-center-rc-xtxfb",
                            "uid": "771842c8-1269-11e9-95a3-005056bb4630",
                            "resourceVersion": "9051577"
                        }
                    },
                    {
                        "ip": "192.169.98.159",
                        "nodeName": "job-node147",
                        "targetRef": {
                            "kind": "Pod",
                            "namespace": "default",
                            "name": "voucher-center-rc-n9wkl",
                            "uid": "77cb9ffc-1269-11e9-95a3-005056bb4630",
                            "resourceVersion": "9051637"
                        }
                    }
                ],
                "ports": [
                    {
                        "name": "beejob-3011",
                        "port": 3011,
                        "protocol": "TCP"
                    },
                    {
                        "name": "server-30012",
                        "port": 8012,
                        "protocol": "TCP"
                    }
                ]
            }
        ]
    }, ]
}
    }
    print(request.POST)
    print(11111)
    choice = request.POST.get('choice')
    # 默认为空时，选择北京
    if not choice:
        choice = 'beijing'


    print(choice)
    data = info_dict.get(choice)
    return HttpResponse(json.dumps(data))
