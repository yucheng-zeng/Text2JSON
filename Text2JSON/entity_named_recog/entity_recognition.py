import sys
from os.path import dirname, abspath
path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(path)
from Text2JSON.entity_named_recog.minute_entity_recognition import minute_recon
from Text2JSON.entity_named_recog.hour_entity_recognition import hour_recon
from Text2JSON.entity_named_recog.day_entity_recognition import day_recon
from Text2JSON.entity_named_recog.month_entity_recognition import month_recon
from Text2JSON.entity_named_recog.quarter_entity_recognition import quart_recon
from Text2JSON.entity_named_recog.year_entity_recognition import year_recon
from Text2JSON.entity_named_recog.proper_noun_recognition import proper_recon
import chinese2digits as ctd
import copy


def entity_recognition(original_line):
    line = copy.deepcopy(original_line)
    line = line.replace('：', ':')
    line = line.replace(' ', '')
    placeholders_list = {}
    line = proper_recon(line, placeholders_list)
    line = minute_recon(line, placeholders_list)
    line = hour_recon(line, placeholders_list)
    line = day_recon(line, placeholders_list)
    line = month_recon(line, placeholders_list)
    line = quart_recon(line, placeholders_list)
    line = year_recon(line, placeholders_list)
    line = ctd.takeChineseNumberFromString(line)['replacedText']
    for holder, data in placeholders_list.items():
        line = line.replace(holder, data[0])
    line = line.replace('““', '“')
    line = line.replace('””', '”')
    return line


if __name__ == '__main__':
    ''
    # example1 = "帮我查一下最近1个月内有哪些范本有新的评价"
    # original_line, line = entity_recognition(example1)
    # print(original_line)
    # print(line)
    # example2 = "我创建一个采购办公用品的合同，金额30万"
    # original_line, line = entity_recognition(example2)
    # print(original_line)
    # print(line)
    # example3 = "帮我用办公用品采购合同范本创建一个合同，金额30万，相对方是北京慧点科技有限公司"
    # original_line, line = entity_recognition(example3)
    # print(original_line)
    # print(line)
    # example4 = "帮我查一下我10月3日提交的“办公用品采购合同”现在到谁审批了"
    # original_line, line = entity_recognition(example4)
    # print(original_line)
    # print(line)
    # example5 = "我正在执行的合同里有哪些合同的相对方最近1个月发生过风险事件"
    # original_line, line = entity_recognition(example5)
    # print(original_line)
    # print(line)
    # example6 = "帮我查一下今年西安分公司销售合同签订的情况（份数、金额）"
    # original_line, line = entity_recognition(example6)
    # print(original_line)
    # print(line)
    # example7 = "今年发生解除的有哪些合同"
    # original_line, line = entity_recognition(example7)
    # print(original_line)
    # print(line)
    # example8 = "帮我导出一下今年合同的台账"
    # original_line, line = entity_recognition(example8)
    # print(original_line)
    # print(line)
    # example9 = "帮我导出本季度, 西安分公司合同的台账，包含合同名称、合同金额、相对方、合同编号"
    # original_line, line = entity_recognition(example9)
    # print(original_line)
    # print(line)
    # example10 = "今年一共发生了多少案件"
    # original_line, line = entity_recognition(example10)
    # print(original_line)
    # print(line)
    # example11 = "有多少案件今年已经结案"
    # original_line, line = entity_recognition(example11)
    # print(original_line)
    # print(line)
    # example12 = "帮我导出今年新发案件的台账"
    # original_line, line = entity_recognition(example12)
    # print(original_line)
    # print(line)
    # example13 = "帮我查一下最近1个月内，上个月和下一个月有哪些范本有新的评价"
    # original_line, line = entity_recognition(example13)
    # print(original_line)
    # print(line)
    # example14 = "帮我查一下本季度，上一季度，下一季度，最近一个季度，上季度，下季度"
    # original_line, line = entity_recognition(example14)
    # print(original_line)
    # print(line)
    # example15 = '15年第1季度，2014年第二季度，2021年第三季度，08年第四季度，1998年第二季度，本季度，上季度，下季度，第一季度，第二季度，第3季度，第4季度'
    # original_line, line = entity_recognition(example15)
    # print(original_line)
    # print(line)
    # example16 = '1月，二月，3月，16年2月，17年12月'
    # original_line, line = entity_recognition(example16)
    # print(original_line)
    # print(line)
    # example17 = '帮我订一个会议室，明天上午9：00 - 11: 30，9人参与，要求有投影仪'
    # original_line, line = entity_recognition(example17)
    # print(original_line)
    # print(line)
    # example18 = '凌晨三点，早上六点，上午八点，中午十二点，下午六点，晚上九点，傍晚五点'
    # original_line, line = entity_recognition(example18)
    # print(original_line)
    # print(line)
    # example19 = '凌晨3点，早上6点，上午8点，中午12点，下午6点，晚上9点，傍晚5点'
    # original_line, line = entity_recognition(example19)
    # print(original_line)
    # print(line)
    # example20 = '凌晨三点二十分，上午八点五十五分，中午十二点十分，下午两点五十五分，晚上九点二十分，傍晚五点半'
    # original_line, line = entity_recognition(example20)
    # print(original_line)
    # print(line)
    # example21 = '凌晨3点，早上6点，上午8点，中午12点，下午6点，晚上9点，傍晚5点'
    # original_line, line = entity_recognition(example21)
    # print(original_line)
    # print(line)
    # example22 = '上午六点五十五分, 早上八点十分， 早上八点零分， 早上八点二十分，早上八点零分'
    # original_line, line = entity_recognition(example22)
    # print(original_line)
    # print(line)
    # example23 = '下午六点五十五分, 傍晚八点十分， 晚上八点零分， 晚上八点十分， 晚上八点零分'
    # original_line, line = entity_recognition(example23)
    # print(original_line)
    # print(line)
    # example24 = '中午十二点五十五分, 正午十一点十分， 正午一点零分， 中午一点十分'
    # original_line, line = entity_recognition(example24)
    # print(original_line)
    # print(line)
    # example24 = '凌晨二点五十五分, 凌晨十一点十分， 凌晨一点零分， 凌晨一点十分'
    # original_line, line = entity_recognition(example24)
    # print(original_line)
    # print(line)
    # example25 = '二点五十五分, 十一点十分， 二十一点零分， 二十四点十分'
    # original_line, line = entity_recognition(example25)
    # print(original_line)
    # print(line)
    # example26 = '二点55分, 十一点10分， 二十一点0分， 二十四点20分'
    # original_line, line = entity_recognition(example26)
    # print(original_line)
    # print(line)
    # example26 = '11日二点55分, 十二日十一点10分， 下一天二十一点0分， 昨天二十四点20分'
    # original_line, line = entity_recognition(example26)
    # print(original_line)
    # print(line)
    # example27 = '十二日十一点10分， 下一天二十一点0分， 昨天二十四点20分'
    # original_line, line = entity_recognition(example27)
    # print(original_line)
    # print(line)
    # example27 = '11日3点55分 - 3点20分'
    # original_line, line = entity_recognition(example27)
    # print(original_line)
    # print(line)
    # example28 = '18年12月11日3点55-4点20'
    # original_line, line = entity_recognition(example28)
    # print(original_line)
    # print(line)
    # example29 = '下午3点五十分'
    # original_line, line = entity_recognition(example29)
    # print(original_line)
    # print(line)
    # example29 = '30分钟后，五分钟后，60分钟前，十分钟前'
    # original_line, line = entity_recognition(example29)
    # print(original_line)
    # print(line)
    # example29 = '5小时前，三十三小时前，14小时后，五小时后'
    # original_line, line = entity_recognition(example29)
    # print(original_line)
    # print(line)
    # example29 = '3天后，十六天后，5天前，十三天前'
    # original_line, line = entity_recognition(example29)
    # print(original_line)
    # print(line)
    #
    # example29 = '3天后下午6点-晚上9点'
    # original_line, line = entity_recognition(example29)
    # print(original_line)
    # print(line)
    #
    # example29 = '下个月6日下午5点30-晚上7点45'
    # original_line, line = entity_recognition(example29)
    # print(original_line)
    # print(line)
