from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
from main import Ui_mainmenu
from logon_mana import Ui_register_2
from logon import Ui_logon
from user import Ui_usermenu
from register import Ui_regist
from managemenu import Ui_manawindow
from manauser import Ui_mana_user
from add_users import Ui_addusers
from delete_users import Ui_deleteusers
from refresh_user import Ui_refreshUser
from mana_flight import Ui_mana_flight
from add_flight import Ui_addFlight
from delete_flight import Ui_deleteflight
from refresh_flight import Ui_refreshFlight
from mana_tickets import Ui_mana_ticket
from mana_ticket_choose import Ui_mana_ticket_choose
from refresh_tickets import Ui_refreshTickets
from mana_orders import Ui_mana_order
from add_orders import  Ui_addOrders
from delete_orders import Ui_deleteorders
from refresh_orders import Ui_refreshOrders
from user_changeinfo import Ui_userchangeinfo
from user_refreshinfo import Ui_userREFRESH
from user_flight import Ui_userflight
from user_order import Ui_userorder
from user_ticket_choose import Ui_user_ticket_choose
from user_buy_flight import Ui_userbuyflight
from user_book import Ui_Form
from user_return import Ui_return_3
from PyQt5.QtGui import *
import pymssql



# 退订
class user_cancelbuy(QWidget,Ui_return_3):
    def __init__(self):
        super(user_cancelbuy, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ret)



    def ret(self):
        global user_sO,now_lg_userid
        rr = self.return_2.text()
        global conn, now_lg_userid
        c1 = conn.cursor()
        c1.execute("SELECT * FROM Orders WHERE 票号='%s' AND 客户编号='%s'" % (rr, now_lg_userid))
        c1_list = c1.fetchall()
        if len(c1_list) == 0:
            reply = QMessageBox.information(self, "注意", "该票号不存在\n请重新输入", QMessageBox.Yes)
        else:
            c1.execute("UPDATE Ticket SET 当前预售状态='未出售' WHERE 票号='%s'" % (c1_list[0][2]))
            conn.commit()
            c1.execute("DELETE FROM Orders WHERE 票号='%s' AND 客户编号='%s'" % (rr,now_lg_userid))
            conn.commit()
            reply = QMessageBox.information(self, "注意", "已成功退票", QMessageBox.Yes)
        user_sO.setstar()
        self.close()




# 预订
class user_Book_Tickets(QWidget,Ui_Form):
    def __init__(self):
        super(user_Book_Tickets, self).__init__()
        self.setupUi(self)
        self.reok.clicked.connect(self.btn)

    def btn(self):
        global conn,now_lg_userid,user_buin
        flight = self.flightid.text()
        fnum = int(self.fnum.text())
        enum = int(self.enum_2.text())
        bnum = int(self.Bnum.text())
        flaggg = 0
        c1 = conn.cursor()
        c1.execute("select * from Flight WHERE 航班号='%s' ORDER BY 航班号" %flight)
        c1l = c1.fetchall()
        if len(c1l)==0:
            reply = QMessageBox.information(self, "注意", "该航线不存在", QMessageBox.Yes)
        c2 = conn.cursor()
        c2.execute("select count(票号) from Ticket WHERE 当前预售状态='未出售' AND 机舱等级='头等舱' AND 航班号='%s' GROUP BY 航班号 ORDER BY 航班号" %flight)
        c2l = c2.fetchall()
        c3 = conn.cursor()
        c3.execute("select count(票号) from Ticket WHERE 当前预售状态='未出售' AND 机舱等级='经济舱' AND 航班号='%s' GROUP BY 航班号 ORDER BY 航班号" %flight)
        c3l = c3.fetchall()
        c4 = conn.cursor()
        c4.execute("select count(票号) from Ticket WHERE 当前预售状态='未出售' AND 机舱等级='商务舱' AND 航班号='%s' GROUP BY 航班号 ORDER BY 航班号" %flight)
        c4l = c4.fetchall()
        c5 = conn.cursor()
        c5.execute('SELECT * FROM Orders')
        c5_list = c5.fetchall()
        idnum = ''
        ofn = ''

        for row in c5_list:
            idnum = row[0]
        ofn += 'ORDER' + str(int(idnum[-5:]) + 1).zfill(5)
        if fnum==0:
            flaggg += 1
        elif fnum>c2l[0][0]:
            reply = QMessageBox.information(self, "注意", "头等舱票数超出可购买范围", QMessageBox.Yes)
        else:
            c1.execute("select 票号 from Ticket WHERE 机舱等级='头等舱' AND 航班号='%s' AND 当前预售状态='未出售'" %flight)
            clist = c1.fetchall()
            num = 0
            cc = conn.cursor()
            for i in clist:
                if num>=fnum:
                    break
                c1.execute("UPDATE Ticket SET 当前预售状态='已出售' WHERE 票号='%s'" % (i[0]))
                conn.commit()
                cc.execute("INSERT INTO Orders(订单号,客户编号,票号,航班号,付款状态) VALUES (%s, %s, %s,%s,%s)",
                           (ofn, now_lg_userid, i[0], flight, '未付款'))
                conn.commit()
            flaggg += 1
        if enum==0:
            flaggg += 1
        elif enum > c3l[0][0]:
            reply = QMessageBox.information(self, "注意", "经济舱票数超出可购买范围", QMessageBox.Yes)
        else:
            c1.execute("select 票号 from Ticket WHERE 机舱等级='经济舱' AND 航班号='%s' AND 当前预售状态='未出售'" %flight)
            clist2 = c1.fetchall()
            cc1 = conn.cursor()
            num2 = 0
            for j in clist2:
                if num2 >= enum:
                    break
                c1.execute("UPDATE Ticket SET 当前预售状态='已出售' WHERE 票号='%s'" % (j[0]))
                conn.commit()
                cc1.execute("INSERT INTO Orders(订单号,客户编号,票号,航班号,付款状态) VALUES (%s, %s, %s,%s,%s)",
                           (ofn, now_lg_userid, j[0], flight, '未付款'))
                conn.commit()
                num2 += 1
            flaggg += 1
        if bnum==0:
            flaggg += 1
        elif bnum > c4l[0][0]:
            reply = QMessageBox.information(self, "注意", "商务舱票数超出可购买范围", QMessageBox.Yes)
        else:
            c1.execute("select 票号 from Ticket WHERE 机舱等级='商务舱' AND 航班号='%s' AND 当前预售状态='未出售'" %flight)
            clist3 = c1.fetchall()
            num3 = 0
            cc2 = conn.cursor()
            for k in clist3:
                if num3 >= bnum:
                    break
                c1.execute("UPDATE Ticket SET 当前预售状态='已出售' WHERE 票号='%s'" % (k[0]))
                conn.commit()
                cc2.execute("INSERT INTO Orders(订单号,客户编号,票号,航班号,付款状态) VALUES (%s, %s, %s,%s,%s)",
                           (ofn, now_lg_userid, k[0], flight, '未付款'))
                conn.commit()
                num3 += 1
            flaggg += 1

        if flaggg==3:
            reply = QMessageBox.information(self, "注意", "购票成功！", QMessageBox.Yes)
            user_buin.setstart()
        self.fnum.clear()
        self.enum_2.clear()
        self.Bnum.clear()
        self.close()




# 用户选择购票地点
class user_choosebuy(QWidget,Ui_user_ticket_choose):
    def __init__(self):
        super(user_choosebuy, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn)

    def btn(self):
        global user_buin,local,purpose,conn
        local=self.go.text()
        purpose=self.purpose.text()
        c1 = conn.cursor()
        c1.execute("select * from Flight WHERE 起飞地点='%s' AND 目的地='%s' ORDER BY 航班号" % (local, purpose))
        c1l = c1.fetchall()
        if len(c1l)==0:
            reply = QMessageBox.information(self, "注意", "该航线不存在", QMessageBox.Yes)
        else:
            user_buin.setstart()
            user_buin.show()
        self.go.clear()
        self.purpose.clear()
        self.close()


# 用户选择购票后的界面
class user_buyinfo(QWidget,Ui_userbuyflight):
    def __init__(self):
        super(user_buyinfo, self).__init__()
        self.setupUi(self)
        self.cancel.clicked.connect(self.exi)
        self.book.clicked.connect(self.booktickets)

        self.model = QStandardItemModel(0, 12)
        # 设置水平方向头标签文本内容
        self.model.setHorizontalHeaderLabels(['航班号', '起飞地点', '目的地', '起飞时间', '落地时间', '起飞日期',
                                              '落地日期', '头等舱机票数', '经济舱机票数', '商务舱机票数', '头等舱剩余票数',
                                              '商务舱剩余票数', '经济舱剩余票数'])
        self.tableView.setModel(self.model)


    def booktickets(self):
        global user_book
        user_book.show()

    def setstart(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['航班号', '起飞地点', '目的地', '起飞时间', '落地时间', '起飞日期',
                                              '落地日期', '头等舱机票数', '经济舱机票数', '商务舱机票数', '头等舱剩余票数',
                                              '商务舱剩余票数', '经济舱剩余票数'])
        global conn,local,purpose
        c1 = conn.cursor()
        c1.execute("select * from Flight WHERE 起飞地点='%s' AND 目的地='%s' ORDER BY 航班号" %(local,purpose))
        c1l = c1.fetchall()
        for row in range(len(c1l)):
            self.model.appendRow([
                QStandardItem('%s' % c1l[row][0]),
                QStandardItem('%s' % c1l[row][1]),
                QStandardItem('%s' % c1l[row][2]),
                QStandardItem('%s' % c1l[row][3]),
                QStandardItem('%s' % c1l[row][4]),
                QStandardItem('%s' % c1l[row][5]),
                QStandardItem('%s' % c1l[row][6]),
                QStandardItem('%s' % c1l[row][7]),
                QStandardItem('%s' % c1l[row][8]),
                QStandardItem('%s' % c1l[row][9])
            ])
            c2 = conn.cursor()
            c2.execute("select count(票号) from Ticket WHERE 当前预售状态='未出售' AND 机舱等级='头等舱' AND 航班号='%s' GROUP BY 航班号 ORDER BY 航班号" %c1l[row][0])
            c2l = c2.fetchall()
            c3 = conn.cursor()
            c3.execute("select count(票号) from Ticket WHERE 当前预售状态='未出售' AND 机舱等级='经济舱' AND 航班号='%s' GROUP BY 航班号 ORDER BY 航班号" %c1l[row][0])
            c3l = c3.fetchall()
            c4 = conn.cursor()
            c4.execute("select count(票号) from Ticket WHERE 当前预售状态='未出售' AND 机舱等级='商务舱' AND 航班号='%s' GROUP BY 航班号 ORDER BY 航班号" %c1l[row][0])
            c4l = c4.fetchall()
            if int(c1l[row][7]) == 0:
                self.model.setItem(row, 10, QStandardItem('0'))
            else:
                self.model.setItem(row, 10, QStandardItem(str(c2l[0][0])))
            if int(c1l[row][8]) == 0:
                self.model.setItem(row, 12, QStandardItem('0'))
            else:
                self.model.setItem(row, 12, QStandardItem(str(c3l[0][0])))
            if int(c1l[row][9]) == 0:
                self.model.setItem(row, 11, QStandardItem('0'))
            else:
                self.model.setItem(row, 11, QStandardItem(str(c4l[0][0])))


    def exi(self):
        global umenu
        self.close()
        umenu.show()



# 用户查询所有订单
class user_searchOrder(QWidget,Ui_userorder):
    def __init__(self):
        super(user_searchOrder, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.exi)
        self.model = QStandardItemModel(0, 13)
        # 设置水平方向头标签文本内容
        self.model.setHorizontalHeaderLabels(['订单号', '票号', '航班号', '付款状态','机舱等级','座位号','票价',
                                              '起飞地点','目的地','起飞时间','落地时间','起飞日期','落地日期'])
        self.tableView.setModel(self.model)

    def setstar(self):
        global conn,now_lg_userid
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['订单号', '票号', '航班号', '付款状态', '机舱等级', '座位号', '票价',
                                              '起飞地点', '目的地', '起飞时间', '落地时间', '起飞日期', '落地日期'])
        c1 = conn.cursor()
        c1.execute("select 订单号,票号,航班号,付款状态 from Orders WHERE 客户编号='%s' ORDER BY 航班号" %now_lg_userid)
        c1l = c1.fetchall()
        for row in range(len(c1l)):
            self.model.appendRow([
                QStandardItem('%s' % c1l[row][0]),
                QStandardItem('%s' % c1l[row][1]),
                QStandardItem('%s' % c1l[row][2]),
                QStandardItem('%s' % c1l[row][3])
            ])
            c2 = conn.cursor()
            c2.execute("select 机舱等级,座位号,票价 from Ticket WHERE 票号='%s' ORDER BY 航班号" %c1l[row][1])
            c2l = c2.fetchall()
            c3 = conn.cursor()
            c3.execute("select 起飞地点,目的地,起飞时间,落地时间,起飞日期,落地日期 from Flight WHERE 航班号='%s' ORDER BY 航班号" %c1l[row][2])
            c3l = c3.fetchall()
            self.model.setItem(row, 4, QStandardItem(c2l[0][0]))
            self.model.setItem(row, 5, QStandardItem(str(c2l[0][1])))
            self.model.setItem(row, 6, QStandardItem(str(c2l[0][2])))
            self.model.setItem(row, 7, QStandardItem(c3l[0][0]))
            self.model.setItem(row, 8, QStandardItem(c3l[0][1]))
            self.model.setItem(row, 9, QStandardItem(c3l[0][2]))
            self.model.setItem(row, 10, QStandardItem(c3l[0][3]))
            self.model.setItem(row, 11, QStandardItem(c3l[0][4]))
            self.model.setItem(row, 12, QStandardItem(c3l[0][5]))


    def exi(self):
        global umenu
        self.close()
        umenu.show()


# 用户查询所有航班
class user_searchFlight(QWidget,Ui_userflight):
    def __init__(self):
        super(user_searchFlight, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.exi)
        self.model = QStandardItemModel(0, 12)
        # 设置水平方向头标签文本内容
        self.model.setHorizontalHeaderLabels(['航班号', '起飞地点', '目的地', '起飞时间', '落地时间', '起飞日期',
                                              '落地日期', '头等舱机票数', '经济舱机票数', '商务舱机票数','头等舱剩余票数',
                                              '商务舱剩余票数','经济舱剩余票数'])
        self.tableView.setModel(self.model)

    def setstart(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['航班号', '起飞地点', '目的地', '起飞时间', '落地时间', '起飞日期',
                                              '落地日期', '头等舱机票数', '经济舱机票数', '商务舱机票数', '头等舱剩余票数',
                                              '商务舱剩余票数', '经济舱剩余票数'])
        global conn
        c1 = conn.cursor()
        c1.execute("select * from Flight ORDER BY 航班号")
        c1l=c1.fetchall()
        c2 = conn.cursor()
        c2.execute("select 航班号,count(票号) from Ticket WHERE 当前预售状态='未出售' AND 机舱等级='头等舱' GROUP BY 航班号 ORDER BY 航班号")
        c2l = c2.fetchall()
        c3 = conn.cursor()
        c3.execute("select 航班号,count(票号) from Ticket WHERE 当前预售状态='未出售' AND 机舱等级='经济舱' GROUP BY 航班号 ORDER BY 航班号")
        c3l = c3.fetchall()
        c4 = conn.cursor()
        c4.execute("select 航班号,count(票号) from Ticket WHERE 当前预售状态='未出售' AND 机舱等级='商务舱' GROUP BY 航班号 ORDER BY 航班号")
        c4l = c4.fetchall()
        for row in range(len(c1l)):
            self.model.appendRow([
                QStandardItem('%s' % c1l[row][0]),
                QStandardItem('%s' % c1l[row][1]),
                QStandardItem('%s' % c1l[row][2]),
                QStandardItem('%s' % c1l[row][3]),
                QStandardItem('%s' % c1l[row][4]),
                QStandardItem('%s' % c1l[row][5]),
                QStandardItem('%s' % c1l[row][6]),
                QStandardItem('%s' % c1l[row][7]),
                QStandardItem('%s' % c1l[row][8]),
                QStandardItem('%s' % c1l[row][9])
            ])
            if int(c1l[row][7])==0:
                self.model.setItem(row, 10, QStandardItem('0'))
            else:
                for i in c2l:
                    if i[0]==c1l[row][0]:
                        temp = int(i[1])
                        c2l.remove(i)
                        break
                self.model.setItem(row, 10, QStandardItem(str(temp)))
            if int(c1l[row][8])==0:
                self.model.setItem(row, 12, QStandardItem('0'))
            else:
                for j in c3l:
                    if j[0]==c1l[row][0]:
                        temp1 = int(j[1])
                        c3l.remove(j)
                        break
                self.model.setItem(row, 12, QStandardItem(str(temp1)))
            if int(c1l[row][9])==0:
                self.model.setItem(row, 11, QStandardItem('0'))
            else:
                for k in c4l:
                    if k[0]==c1l[row][0]:
                        temp2 = int(k[1])
                        c4l.remove(k)
                        break
                self.model.setItem(row, 11, QStandardItem(str(temp2)))

    def exi(self):
        global umenu
        self.close()
        umenu.show()


# 更新用户信息
class user_chRefresh(QWidget,Ui_userREFRESH):
    def __init__(self):
        super(user_chRefresh, self).__init__()
        self.setupUi(self)
        self.reok.clicked.connect(self.btn)


    def btn(self):
        name = self.username.text()
        birth = self.userbirth.text()
        sex = self.usersex.text()
        number = self.usernum.text()
        itype = self.usertype.text()
        inum = self.useridnum.text()
        pay = self.userpay.text()
        pas = self.userpassword.text()
        global conn, now_lg_userid
        c1 = conn.cursor()
        c1.execute("SELECT * FROM Client")
        c1_list = c1.fetchall()
        for row in c1_list:
            if row[0] == now_lg_userid:
                flag = 0
                break
        if flag == 1:
            reply = QMessageBox.information(self, "注意", "该账号不存在\n请重新输入", QMessageBox.Yes)
        elif flag == 0:
            c1.execute("UPDATE Client SET 客户姓名 = '%s', 客户出生日期='%s', 性别='%s', 联系方式='%s', 证件类型='%s', 证件号码='%s',付款方式='%s', 客户密码='%s' WHERE 客户编号 = '%s'" %(name,birth,sex,number,itype,inum,pay,pas,now_lg_userid))
            conn.commit()
            reply = QMessageBox.information(self, "注意", "已成功更新", QMessageBox.Yes)
        self.username.clear()
        self.userbirth.clear()
        self.usersex.clear()
        self.usernum.clear()
        self.usertype.clear()
        self.useridnum.clear()
        self.userpay.clear()
        self.userpassword.clear()
        self.close()


    def refresh_all(self):
        global conn, now_lg_userid
        c1 = conn.cursor()
        c1.execute("select 客户姓名,客户出生日期,性别,联系方式,证件类型,证件号码,付款方式,客户密码 from Client WHERE 客户编号='%s'" % now_lg_userid)
        clist = c1.fetchall()
        self.username.setText(clist[0][0])
        self.userbirth.setText(clist[0][1])
        self.usersex.setText(clist[0][2])
        self.usernum.setText(clist[0][3])
        self.usertype.setText(clist[0][4])
        self.useridnum.setText(clist[0][5])
        self.userpay.setText(clist[0][6])
        self.userpassword.setText(clist[0][7])


# 用户更新信息
class user_reinfo(QWidget,Ui_userchangeinfo):
    def __init__(self):
        super(user_reinfo, self).__init__()
        self.setupUi(self)
        self.refresh.clicked.connect(self.re)
        self.cancel.clicked.connect(self.exi)
        self.model = QStandardItemModel(0, 8)
        global now_lg_userid
        # 设置水平方向头标签文本内容
        self.model.setHorizontalHeaderLabels(['客户姓名', '客户出生日期', '性别', '联系方式', '证件类型',
                                              '证件号码', '付款方式','客户密码'])
        self.tableView.setModel(self.model)


    def re(self):
        global conn, user_cinfo
        user_cinfo.refresh_all()
        user_cinfo.show()

    def exi(self):
        global umenu
        self.close()
        umenu.show()

    def refreshall(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['客户姓名', '客户出生日期', '性别', '联系方式', '证件类型',
                                              '证件号码', '付款方式', '客户密码'])
        global conn
        c1 = conn.cursor()
        c1.execute("select 客户姓名,客户出生日期,性别,联系方式,证件类型,证件号码,付款方式,客户密码 from Client WHERE 客户编号='%s'" % now_lg_userid)
        for row in c1:
            self.model.appendRow([
                QStandardItem('%s' % row[0]),
                QStandardItem('%s' % row[1]),
                QStandardItem('%s' % row[2]),
                QStandardItem('%s' % row[3]),
                QStandardItem('%s' % row[4]),
                QStandardItem('%s' % row[5]),
                QStandardItem('%s' % row[6]),
                QStandardItem('%s' % row[7])
            ])


# 更新订单
class refO(QWidget,Ui_refreshOrders):
    def __init__(self):
        super(refO, self).__init__()
        self.setupUi(self)
        self.reok.clicked.connect(self.btn)

    def btn(self):
        global conn
        id = self.orderid.text()
        uid = self.userid.text()
        tid = self.ticketid.text()
        fid = self.flightid.text()
        ps = self.paystate.text()
        c1 = conn.cursor()
        c1.execute("SELECT 订单号,票号 FROM Orders WHERE 订单号='%s'" %id)
        c1_list = c1.fetchall()
        flag = 1
        oldtid = []
        for row in c1_list:
            if row[0] == id:
                flag = 0
                oldtid.append(row[1])
        if flag == 1:
            reply = QMessageBox.information(self, "注意", "该订单号不存在\n请重新输入", QMessageBox.Yes)
        elif flag == 0:
            try:
                if tid!=oldtid:
                    c1.execute("UPDATE Ticket SET 当前预售状态='未出售' WHERE 票号='%s'"%(oldtid))
                    conn.commit()
                    c1.execute("UPDATE Ticket SET 当前预售状态='已出售' WHERE 票号='%s'"%(tid))
                    conn.commit()
                c1.execute(
                    "UPDATE Orders SET 客户编号='%s',票号='%s',航班号='%s',付款状态='%s' WHERE 订单号='%s'"
                    %(uid, tid, fid, ps, id))
                conn.commit()
                reply = QMessageBox.information(self, "注意", "更新成功！", QMessageBox.Yes)
            except:
                conn.rollback()
        self.orderid.clear()
        self.userid.clear()
        self.ticketid.clear()
        self.flightid.clear()
        self.paystate.clear()
        self.close()

#删除订单
class deleteO(QWidget,Ui_deleteorders):
    def __init__(self):
        super(deleteO, self).__init__()
        self.setupUi(self)
        self.delok.clicked.connect(self.btn)

    def btn(self):
        num = self.userid.text()
        global conn
        flag = 1
        c1 = conn.cursor()
        c1.execute('SELECT 订单号 FROM Orders')
        c1_list = c1.fetchall()
        for row in c1_list:
            if row[0] == num:
                flag = 0
                break
        if flag == 1:
            reply = QMessageBox.information(self, "注意", "该订单号不存在\n请重新输入", QMessageBox.Yes)
        elif flag == 0:
            c1.execute("UPDATE Ticket SET 当前预售状态='未出售' WHERE 票号 in (SELECT 票号 FROM Orders WHERE 订单号='%s'))" %(num))
            conn.commit()
            c1.execute("DELETE FROM Orders WHERE 订单号=%s", (num))
            conn.commit()
            reply = QMessageBox.information(self, "注意", "已成功删除", QMessageBox.Yes)
        self.userid.clear()
        self.close()

# 增加订单
class addO(QWidget,Ui_addOrders):
    def __init__(self):
        super(addO, self).__init__()
        self.setupUi(self)
        self.reok.clicked.connect(self.btn)

    def btn(self):
        global conn
        id = self.orderid.text()
        uid = self.userid.text()
        tid = self.ticketid.text()
        fid = self.flightid.text()
        ps = self.paystate.text()
        c1 = conn.cursor()
        c1.execute('SELECT 订单号 FROM Orders')
        c1_list = c1.fetchall()
        flag = 1
        for row in c1_list:
            if row[0] == id:
                flag = 0
        if flag == 1:
            try:
                c1.execute("SELECT 客户编号 FROM Client WHERE 客户编号='%s'" %uid)
                c1_l = c1.fetchall()
                c1.execute("SELECT 航班号 FROM Flight WHERE 航班号='%s'" % fid)
                c1_l2 = c1.fetchall()
                c1.execute("SELECT 票号 FROM Ticket WHERE 票号='%s'" % tid)
                c1_l3 = c1.fetchall()
                if len(c1_l)==0:
                    reply = QMessageBox.information(self, "注意", "该客户不存在\n请重新输入", QMessageBox.Yes)
                elif len(c1_l2)==0:
                    reply = QMessageBox.information(self, "注意", "该航班不存在\n请重新输入", QMessageBox.Yes)
                elif len(c1_l3)==0:
                    reply = QMessageBox.information(self, "注意", "该机票不存在\n请重新输入", QMessageBox.Yes)
                else:
                    c1.execute("INSERT INTO Orders(订单号,客户编号,票号,航班号,付款状态) VALUES (%s, %s, %s,%s,%s)", (id, uid, tid,fid,ps))
                    conn.commit()
                    c1.execute("UPDATE Ticket SET 当前预售状态='已出售' WHERE 票号 in (SELECT 票号 FROM Orders WHERE 订单号='%s')" %id)
                    conn.commit()
                    reply = QMessageBox.information(self, "注意", "添加成功！", QMessageBox.Yes)
            except:
                conn.rollback()
        self.orderid.clear()
        self.userid.clear()
        self.ticketid.clear()
        self.flightid.clear()
        self.paystate.clear()
        self.close()


# 管理订单
class Mana_Order(QWidget,Ui_mana_order):
    def __init__(self):
        super(Mana_Order,self).__init__()
        self.setupUi(self)
        self.model = QStandardItemModel(0, 5)
        # 设置水平方向头标签文本内容
        self.model.setHorizontalHeaderLabels(['订单号', '客户编号', '票号', '航班号', '付款状态'])
        self.userview.setModel(self.model)
        global conn
        c1 = conn.cursor()
        c1.execute("select * from Orders")
        for row in c1:
            self.model.appendRow([
                QStandardItem('%s' % row[0]),
                QStandardItem('%s' % row[1]),
                QStandardItem('%s' % row[2]),
                QStandardItem('%s' % row[3]),
                QStandardItem('%s' % row[4])
            ])
        self.add.clicked.connect(self.add_orders)
        self.delete_2.clicked.connect(self.deleteo)
        self.refresh.clicked.connect(self.ref)
        self.return_2.clicked.connect(self.return_back)

    def ref(self):
        global mana_reO,mana_t,mana_f
        mana_t.refresh_all()
        mana_f.refresh_all()
        mana_reO.show()

    def add_orders(self):
        global mana_aO,mana_t,mana_f
        mana_t.refresh_all()
        mana_f.refresh_all()
        mana_aO.show()

    def refresh_all(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['订单号', '客户编号', '票号', '航班号', '付款状态'])
        global conn
        c1 = conn.cursor()
        c1.execute("select * from Orders")
        for row in c1:
            self.model.appendRow([
                QStandardItem('%s' % row[0]),
                QStandardItem('%s' % row[1]),
                QStandardItem('%s' % row[2]),
                QStandardItem('%s' % row[3]),
                QStandardItem('%s' % row[4])
            ])


    def deleteo(self):
        global mana_deleO,mana_t,mana_f
        mana_t.refresh_all()
        mana_f.refresh_all()
        mana_deleO.show()


    def return_back(self):
        global mana_o, manamenu
        mana_o.close()
        manamenu.show()



# 更新机票
class refT(QWidget,Ui_refreshTickets):
    def __init__(self):
        super(refT, self).__init__()
        self.setupUi(self)
        self.reok.clicked.connect(self.btn)

    def btn(self):
        global conn,re_ticket_id
        price = self.ticketprice.text()
        discount = self.discount.text()
        sellstate = self.state.text()
        c1 = conn.cursor()
        try:
            c1.execute(
                "UPDATE Ticket SET 票价='%s',折扣='%s',当前预售状态='%s' WHERE 票号='%s'"
                %(price, discount, sellstate, re_ticket_id))
            conn.commit()
            reply = QMessageBox.information(self, "注意", "更新成功！", QMessageBox.Yes)
        except:
            conn.rollback()
        self.ticketprice.clear()
        self.discount.clear()
        self.state.clear()
        self.close()


# 选择更新的票号
class chooT(QWidget,Ui_mana_ticket_choose):
    def __init__(self):
        super(chooT, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn)


    def btn(self):
        global mana_reT,re_ticket_id,conn
        re_ticket_id = self.lineEdit.text()
        c1 = conn.cursor()
        c1.execute('SELECT 票号 FROM Ticket')
        c1_list = c1.fetchall()
        flag = 1
        for row in c1_list:
            if row[0] == re_ticket_id:
                flag = 0
                break
        if flag == 1:
            reply = QMessageBox.information(self, "注意", "该票号不存在\n请重新输入", QMessageBox.Yes)
        else:
            mana_reT.show()
        self.close()



# 管理机票
class Mana_Tick(QWidget,Ui_mana_ticket):
    def __init__(self):
        super(Mana_Tick,self).__init__()
        self.setupUi(self)
        self.model = QStandardItemModel(0, 7)
        # 设置水平方向头标签文本内容
        self.model.setHorizontalHeaderLabels(['票号', '航班号', '票价', '机舱等级', '座位号','折扣',
                                              '当前预售状态'])
        self.userview.setModel(self.model)
        global conn
        c1 = conn.cursor()
        c1.execute("select * from Ticket")
        for row in c1:
            self.model.appendRow([
                QStandardItem('%s' % row[0]),
                QStandardItem('%s' % row[1]),
                QStandardItem('%s' % row[2]),
                QStandardItem('%s' % row[3]),
                QStandardItem('%s' % row[4]),
                QStandardItem('%s' % row[5]),
                QStandardItem('%s' % row[6])
            ])
        self.refresh.clicked.connect(self.ref)
        self.return_2.clicked.connect(self.return_back)

    def ref(self):
        global mana_ct
        mana_ct.show()

    def refresh_all(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['票号', '航班号', '票价', '机舱等级', '座位号','折扣',
                                              '当前预售状态'])
        global conn
        c1 = conn.cursor()
        c1.execute("select * from Ticket")
        for row in c1:
            self.model.appendRow([
                QStandardItem('%s' % row[0]),
                QStandardItem('%s' % row[1]),
                QStandardItem('%s' % row[2]),
                QStandardItem('%s' % row[3]),
                QStandardItem('%s' % row[4]),
                QStandardItem('%s' % row[5]),
                QStandardItem('%s' % row[6])
            ])


    def return_back(self):
        global mana_t, manamenu
        mana_t.close()
        manamenu.show()


# 更新航班
class refF(QWidget,Ui_refreshFlight):
    def __init__(self):
        super(refF, self).__init__()
        self.setupUi(self)
        self.reok.clicked.connect(self.btn)


    def btn(self):
        global conn
        id = self.flightid.text()
        start = self.start.text()
        end = self.end.text()
        stime = self.stime.text()
        etime = self.etime.text()
        sdate = self.sdate.text()
        edate = self.edate.text()
        fnum = self.fnum.text()
        enum_2 = self.enum_2.text()
        bnum = self.Bnum.text()
        c1 = conn.cursor()
        c1.execute('SELECT 航班号 FROM Flight')
        c1_list = c1.fetchall()
        flag = 1
        for row in c1_list:
            if row[0] == id:
                flag = 0
                break
        if flag == 1:
            reply = QMessageBox.information(self, "注意", "该航班号不存在\n请重新输入", QMessageBox.Yes)
        elif flag == 0:
            try:
                c1.execute(
                    "UPDATE Flight SET 起飞地点='%s',目的地='%s',起飞时间='%s',落地时间='%s',起飞日期='%s',落地日期='%s',头等舱机票数='%s',经济舱机票数='%s',商务舱机票数='%s' WHERE 航班号='%s'"
                    %(start, end, stime, etime, sdate, edate, fnum, enum_2, bnum, id))
                conn.commit()
                reply = QMessageBox.information(self, "注意", "更新成功！", QMessageBox.Yes)
            except:
                conn.rollback()
        self.flightid.clear()
        self.start.clear()
        self.end.clear()
        self.stime.clear()
        self.etime.clear()
        self.sdate.clear()
        self.edate.clear()
        self.fnum.clear()
        self.enum_2.clear()
        self.Bnum.clear()
        self.close()

#删除航班
class deleteF(QWidget,Ui_deleteflight):
    def __init__(self):
        super(deleteF, self).__init__()
        self.setupUi(self)
        self.delok.clicked.connect(self.btn)

    def btn(self):
        num = self.userid.text()
        global conn
        flag = 1
        c1 = conn.cursor()
        c1.execute('SELECT 航班号 FROM Flight')
        c1_list = c1.fetchall()
        for row in c1_list:
            if row[0] == num:
                flag = 0
                break
        if flag == 1:
            reply = QMessageBox.information(self, "注意", "该航班号不存在\n请重新输入", QMessageBox.Yes)
        elif flag == 0:
            c1.execute("DELETE FROM Ticket WHERE 航班号=%s", (num))
            conn.commit()
            c2 = conn.cursor()
            c2.execute("DELETE FROM Flight WHERE 航班号=%s", (num))
            conn.commit()
            reply = QMessageBox.information(self, "注意", "已成功删除", QMessageBox.Yes)
        self.userid.clear()
        self.close()


# 增加航班
class addF(QWidget,Ui_addFlight):
    def __init__(self):
        super(addF, self).__init__()
        self.setupUi(self)
        self.reok.clicked.connect(self.btn)

    def btn(self):
        global conn
        id = self.flightid.text()
        start = self.start.text()
        end = self.end.text()
        stime = self.stime.text()
        etime = self.etime.text()
        sdate = self.sdate.text()
        edate = self.edate.text()
        fnum = self.fnum.text()
        enum_2 = self.enum_2.text()
        bnum = self.Bnum.text()
        tflag = self.tflag.text()
        fprice = self.Fprice.text()
        bprice = self.Bprice.text()
        eprice = self.Eprice.text()

        c1 = conn.cursor()
        c1.execute('SELECT 航班号 FROM Flight')
        c1_list = c1.fetchall()
        flag = 1
        for row in c1_list:
            if row[0] == id:
                flag = 0
                break
        if flag == 0:
            reply = QMessageBox.information(self, "注意", "该航班号已存在\n请重新输入", QMessageBox.Yes)
        elif flag == 1:
            try:
                c1.execute("INSERT INTO Flight(航班号,起飞地点,目的地,起飞时间,落地时间,起飞日期,落地日期,头等舱机票数,经济舱机票数,商务舱机票数) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s)", (id, start, end,stime,etime,sdate,edate,fnum,enum_2,bnum))
                conn.commit()
                ttid = 1
                if fnum=='':
                    temp1 = 0
                else:
                    temp1 = int(fnum)
                if enum_2=='':
                    temp2 = 0
                else:
                    temp2 = int(enum_2)
                if bnum=='':
                    temp3 = 0
                else:
                    temp3 = int(bnum)
                for i in range(temp1):
                    c1.execute(
                        "INSERT INTO Ticket(票号,航班号,票价,机舱等级,座位号,折扣,当前预售状态) VALUES (%s, %s, %s,%s,%s,%s,%s)",
                        (tflag+str(ttid).zfill(3), id, fprice, '头等舱', i+1, 0,'未出售'))
                    conn.commit()
                    ttid+=1
                for j in range(temp2):
                    c1.execute(
                        "INSERT INTO Ticket(票号,航班号,票价,机舱等级,座位号,折扣,当前预售状态) VALUES (%s, %s, %s,%s,%s,%s,%s)",
                        (tflag+str(ttid).zfill(3), id, bprice, '商务舱', j+1, 0,'未出售'))
                    conn.commit()
                    ttid += 1
                for k in range(temp3):
                    c1.execute(
                        "INSERT INTO Ticket(票号,航班号,票价,机舱等级,座位号,折扣,当前预售状态) VALUES (%s, %s, %s,%s,%s,%s,%s)",
                        (tflag+str(ttid).zfill(3), id, eprice, '经济舱', k+1, 0,'未出售'))
                    conn.commit()
                    ttid += 1

                reply = QMessageBox.information(self, "注意", "添加成功！", QMessageBox.Yes)
            except:
                conn.rollback()
        self.flightid.clear()
        self.start.clear()
        self.end.clear()
        self.stime.clear()
        self.etime.clear()
        self.sdate.clear()
        self.edate.clear()
        self.fnum.clear()
        self.enum_2.clear()
        self.Bnum.clear()
        self.close()


# 管理航班
class Mana_Flig(QWidget,Ui_mana_flight):
    def __init__(self):
        super(Mana_Flig,self).__init__()
        self.setupUi(self)
        self.model = QStandardItemModel(0, 10)
        # 设置水平方向头标签文本内容
        self.model.setHorizontalHeaderLabels(['航班号', '起飞地点', '目的地', '起飞时间', '落地时间','起飞日期',
                                              '落地日期','头等舱机票数', '经济舱机票数', '商务舱机票数'])
        self.userview.setModel(self.model)
        global conn
        c1 = conn.cursor()
        c1.execute("select * from Flight")
        for row in c1:
            self.model.appendRow([
                QStandardItem('%s' % row[0]),
                QStandardItem('%s' % row[1]),
                QStandardItem('%s' % row[2]),
                QStandardItem('%s' % row[3]),
                QStandardItem('%s' % row[4]),
                QStandardItem('%s' % row[5]),
                QStandardItem('%s' % row[6]),
                QStandardItem('%s' % row[7]),
                QStandardItem('%s' % row[8]),
                QStandardItem('%s' % row[9])
            ])
        self.add.clicked.connect(self.add_flight)
        self.delete_2.clicked.connect(self.deletef)
        self.refresh.clicked.connect(self.ref)
        self.return_2.clicked.connect(self.return_back)

    def ref(self):
        global mana_reF,mana_t
        mana_t.refresh_all()
        mana_reF.show()

    def add_flight(self):
        global mana_aF,mana_t
        mana_t.refresh_all()
        mana_aF.show()

    def refresh_all(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['航班号', '起飞地点', '目的地', '起飞时间', '落地时间','起飞日期',
                                              '落地日期','头等舱机票数', '经济舱机票数', '商务舱机票数'])
        global conn
        c1 = conn.cursor()
        c1.execute("select * from Flight")
        for row in c1:
            self.model.appendRow([
                QStandardItem('%s' % row[0]),
                QStandardItem('%s' % row[1]),
                QStandardItem('%s' % row[2]),
                QStandardItem('%s' % row[3]),
                QStandardItem('%s' % row[4]),
                QStandardItem('%s' % row[5]),
                QStandardItem('%s' % row[6]),
                QStandardItem('%s' % row[7]),
                QStandardItem('%s' % row[8]),
                QStandardItem('%s' % row[9])
            ])


    def deletef(self):
        global mana_deleF,mana_t
        mana_t.refresh_all()
        mana_deleF.show()


    def return_back(self):
        global mana_f, manamenu
        mana_f.close()
        manamenu.show()

# 更新用户
class User_Change(QWidget,Ui_refreshUser):
    def __init__(self):
        super(User_Change, self).__init__()
        self.setupUi(self)
        self.reok.clicked.connect(self.btn)


    def btn(self):
        idnum = self.userid.text()
        name = self.username.text()
        birth = self.userbirth.text()
        sex = self.usersex.text()
        number = self.usernum.text()
        itype = self.usertype.text()
        inum = self.useridnum.text()
        pay = self.userpay.text()
        pas = self.userpassword.text()
        global conn
        c1 = conn.cursor()
        c1.execute("SELECT * FROM Client")
        c1_list = c1.fetchall()
        for row in c1_list:
            if row[0] == idnum:
                flag = 0
                break
        if flag == 1:
            reply = QMessageBox.information(self, "注意", "该账号不存在\n请重新输入", QMessageBox.Yes)
        elif flag == 0:
            c1.execute("UPDATE Client SET 客户姓名 = '%s', 客户出生日期='%s', 性别='%s', 联系方式='%s', 证件类型='%s', 证件号码='%s',付款方式='%s', 客户密码='%s' WHERE 客户编号 = '%s'" %(name,birth,sex,number,itype,inum,pay,pas,idnum))
            conn.commit()
            reply = QMessageBox.information(self, "注意", "已成功更新", QMessageBox.Yes)
        self.userid.clear()
        self.username.clear()
        self.userbirth.clear()
        self.usersex.clear()
        self.usernum.clear()
        self.usertype.clear()
        self.useridnum.clear()
        self.userpay.clear()
        self.userpassword.clear()
        self.close()

#删除用户
class deleteU(QWidget,Ui_deleteusers):
    def __init__(self):
        super(deleteU, self).__init__()
        self.setupUi(self)
        self.delok.clicked.connect(self.btn)

    def btn(self):
        num = self.userid.text()
        global conn
        flag = 1
        c1 = conn.cursor()
        c1.execute('SELECT 客户编号 FROM Client')
        c1_list = c1.fetchall()
        for row in c1_list:
            if row[0] == num:
                flag = 0
                break
        if flag == 1:
            reply = QMessageBox.information(self, "注意", "该账号不存在\n请重新输入", QMessageBox.Yes)
        elif flag == 0:
            c1.execute("DELETE FROM Client WHERE 客户编号=%s", (num))
            conn.commit()
            reply = QMessageBox.information(self, "注意", "已成功删除", QMessageBox.Yes)
        self.userid.clear()
        self.close()

# 增加用户
class addU(QWidget,Ui_addusers):
    def __init__(self):
        super(addU, self).__init__()
        self.setupUi(self)
        self.adOk.clicked.connect(self.btn)

    def btn(self):
        global conn
        id = self.userid.text()
        pa = self.userpassword.text()
        c1 = conn.cursor()
        c1.execute('SELECT 客户编号,客户账号,客户密码 FROM Client')
        c1_list = c1.fetchall()
        flag = 1
        num = ''
        idnum = ''
        for row in c1_list:
            if row[1] == id:
                flag = 0
            idnum = row[0]
        if flag == 0:
            reply = QMessageBox.information(self, "注意", "该账号已存在\n请重新输入", QMessageBox.Yes)
        elif flag == 1:
            try:
                num += 'CLIEN' + str(int(idnum[-5:]) + 1).zfill(5)
                c1.execute("INSERT INTO Client(客户编号,客户账号,客户密码) VALUES (%s, %s, %s)", (num, id, pa))
                conn.commit()
                reply = QMessageBox.information(self, "注意", "添加成功！", QMessageBox.Yes)
            except:
                conn.rollback()
        self.userid.clear()
        self.userpassword.clear()
        self.close()


# 管理用户
class Mana_User(QWidget,Ui_mana_user):
    def __init__(self):
        super(Mana_User,self).__init__()
        self.setupUi(self)
        #self.user_4.clicked.connect(self.exit)
        self.model = QStandardItemModel(0, 10)
        # 设置水平方向头标签文本内容
        self.model.setHorizontalHeaderLabels(['客户编号', '客户姓名', '客户出生日期', '性别', '联系方式','证件类型',
                                              '证件号码','付款方式', '客户账号', '客户密码'])
        self.userview.setModel(self.model)
        global conn
        c1 = conn.cursor()
        c1.execute("select * from Client")
        for row in c1:
            self.model.appendRow([
                QStandardItem('%s' % row[0]),
                QStandardItem('%s' % row[1]),
                QStandardItem('%s' % row[2]),
                QStandardItem('%s' % row[3]),
                QStandardItem('%s' % row[4]),
                QStandardItem('%s' % row[5]),
                QStandardItem('%s' % row[6]),
                QStandardItem('%s' % row[7]),
                QStandardItem('%s' % row[8]),
                QStandardItem('%s' % row[9])
            ])
        self.add.clicked.connect(self.add_user)
        self.delete_2.clicked.connect(self.deleteU)
        self.refresh.clicked.connect(self.ref)
        self.return_2.clicked.connect(self.return_back)


    def ref(self):
        global User_C
        User_C.show()


    def add_user(self):
        global mana_aU
        mana_aU.show()

    def refresh_all(self):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['客户编号', '客户姓名', '客户出生日期', '性别', '联系方式', '证件类型',
                                              '证件号码', '付款方式', '客户账号', '客户密码'])
        global conn
        c1 = conn.cursor()
        c1.execute("select * from Client")
        for row in c1:
            self.model.appendRow([
                QStandardItem('%s' % row[0]),
                QStandardItem('%s' % row[1]),
                QStandardItem('%s' % row[2]),
                QStandardItem('%s' % row[3]),
                QStandardItem('%s' % row[4]),
                QStandardItem('%s' % row[5]),
                QStandardItem('%s' % row[6]),
                QStandardItem('%s' % row[7]),
                QStandardItem('%s' % row[8]),
                QStandardItem('%s' % row[9])
            ])


    def deleteU(self):
        global mana_deleU
        mana_deleU.show()


    def return_back(self):
        global mana_u, manamenu
        mana_u.close()
        manamenu.show()




# 管理员菜单
class ManaMenu(QMainWindow,Ui_manawindow):
    def __init__(self):
        super(ManaMenu,self).__init__()
        self.setupUi(self)
        self.user_4.clicked.connect(self.exit)
        self.manamenu.clicked.connect(self.user_manage)
        self.flight.clicked.connect(self.flight_manage)
        self.ticket.clicked.connect(self.ticket_manage)
        self.order.clicked.connect(self.order_manage)


    def exit(self):
        global manamenu, ui
        reply = QMessageBox.information(self, "注意", "是否要退出？", QMessageBox.Yes|QMessageBox.No)
        if reply==QMessageBox.Yes:
            manamenu.close()
            ui.show()
        else:
            pass

    def user_manage(self):
        global mana_u
        mana_u.show()
        self.hide()

    def flight_manage(self):
        global mana_f
        mana_f.show()
        self.hide()

    def ticket_manage(self):
        global mana_t
        mana_t.show()
        self.hide()

    def order_manage(self):
        global mana_o
        mana_o.show()


# 管理员登录
class ManaLogon(QWidget,Ui_register_2):
    def __init__(self):
        super(ManaLogon,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnClick)  # 按钮事件绑定

    # 子窗体自定义事件
    def btnClick(self):
        global conn,manamenu,ui
        id = self.manaid.text()
        pa = self.manapassword.text()
        c1=conn.cursor()
        c1.execute('SELECT 管理员账号,管理员密码 FROM Manager')
        flag = 1
        for row in c1:
            if row[0]==id and row[1]==pa:
                flag = 0
                break
        if flag==1:
            reply = QMessageBox.information(self, "注意", "该管理员账号不存在\n请检查账号和密码", QMessageBox.Yes)
        elif flag==0:
            manamenu.show()
            ui.close()
        self.manaid.clear()
        self.manapassword.clear()
        self.close()


# 用户注册
class Userregi(QWidget,Ui_regist):
    def __init__(self):
        super(Userregi,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnClick)  # 按钮事件绑定


    # 子窗体自定义事件
    def btnClick(self):
        global umenu, ui,conn
        id = self.userid.text()
        pa = self.userpassword.text()
        c1 = conn.cursor()
        c1.execute('SELECT 客户编号,客户账号,客户密码 FROM Client')
        c1_list = c1.fetchall()
        flag = 1
        num=''
        idnum = ''
        for row in c1_list:
            if row[1] == id:
                flag = 0
            idnum = row[0]
        if flag == 0:
            reply = QMessageBox.information(self, "注意", "该账号已存在\n请重新注册", QMessageBox.Yes)
        elif flag == 1:
            try:
                num += 'CLIEN' + str(int(idnum[-5:])+1).zfill(5)
                c1.execute("INSERT INTO Client(客户编号,客户账号,客户密码) VALUES (%s, %s, %s)",(num, id, pa))
                conn.commit()
                reply = QMessageBox.information(self, "注意", "注册成功，请登录！", QMessageBox.Yes)
            except:
                conn.rollback()
        self.userid.clear()
        self.userpassword.clear()
        self.close()


# 用户菜单
class UserMenu(QMainWindow,Ui_usermenu):
    def __init__(self):
        super(UserMenu,self).__init__()
        self.setupUi(self)
        self.exit.clicked.connect(self.exitwindow)
        self.changeinfo.clicked.connect(self.change_info)
        self.checkflight.clicked.connect(self.search_flight)
        self.checkorder.clicked.connect(self.search_order)
        self.order.clicked.connect(self.ticket_buy)
        self.cancelorder.clicked.connect(self.ticket_back)


    def change_info(self):
        global user_info
        user_info.refreshall()
        user_info.show()
        self.hide()

    def search_flight(self):
        global user_sF
        user_sF.setstart()
        user_sF.show()

    def search_order(self):
        global user_sO
        user_sO.setstar()
        user_sO.show()

    def ticket_buy(self):
        global user_cb
        user_cb.show()

    def ticket_back(self):
        global user_can
        user_can.show()

    def exitwindow(self):
        global umenu, ui
        reply = QMessageBox.information(self, "注意", "是否要退出？", QMessageBox.Yes|QMessageBox.No)
        if reply==QMessageBox.Yes:
            umenu.close()
            ui.show()
        else:
            pass


# 用户登录
class Ulogon(QWidget,Ui_logon):
    def __init__(self):
        super(Ulogon,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnClick)  # 按钮事件绑定


    # 子窗体自定义事件
    def btnClick(self):
        global conn, umenu, ui, now_lg_userid
        id = self.userid.text()
        pa = self.userpassword.text()
        c1 = conn.cursor()
        c1.execute('SELECT 客户编号,客户账号,客户密码 FROM Client')
        flag = 1
        for row in c1:
            if row[1] == id and row[2] == pa:
                flag = 0
                now_lg_userid = row[0]
                break
        if flag == 1:
            reply = QMessageBox.information(self, "注意", "该客户账号不存在\n请检查账号和密码", QMessageBox.Yes)
        elif flag == 0:
            umenu.show()
            ui.close()
        self.userid.clear()
        self.userpassword.clear()
        self.close()

# 主界面
class MainWidget(QMainWindow,Ui_mainmenu):
    def __init__(self):
        super(MainWidget,self).__init__()
        self.setupUi(self)





if  __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)

    # 更新机票号
    re_ticket_id = 0

    # 当前登录的用户编号
    now_lg_userid = 0

    # 用户购票的出发点、目的地
    local = ''
    purpose = ''

    server = 'AMY-VAIO'
    user = 'admin'
    password = '1'
    database = 'DB'

    conn = pymssql.connect(server, user, password, database)

    ui = MainWidget()

    ulg = Ulogon()

    umenu = UserMenu()

    urg = Userregi()

    manalg = ManaLogon()

    manamenu = ManaMenu()

    mana_u = Mana_User()

    mana_deleU = deleteU()

    mana_aU = addU()

    User_C = User_Change()

    mana_f = Mana_Flig()

    mana_aF = addF()

    mana_deleF = deleteF()

    mana_reF = refF()

    mana_reT = refT()

    mana_t = Mana_Tick()

    mana_ct = chooT()

    mana_reO = refO()

    mana_aO = addO()

    mana_deleO = deleteO()

    mana_o = Mana_Order()

    user_info = user_reinfo()

    user_cinfo = user_chRefresh()

    user_sF = user_searchFlight()

    user_sO = user_searchOrder()

    user_cb = user_choosebuy()

    user_buin = user_buyinfo()

    user_book = user_Book_Tickets()

    user_can = user_cancelbuy()

    # 点击用户登录
    userlogon = ui.logon
    userlogon.clicked.connect(ulg.show)

    # 点击用户注册
    userregist = ui.register_2
    userregist.clicked.connect(urg.show)

    # 点击管理员登录
    manalog = ui.manalogon
    manalog.clicked.connect(manalg.show)

    # 管理员管理用户
    mana_aU.adOk.clicked.connect(mana_u.refresh_all)
    mana_deleU.delok.clicked.connect(mana_u.refresh_all)
    User_C.reok.clicked.connect(mana_u.refresh_all)
    # 管理员管理航班
    mana_aF.reok.clicked.connect(mana_f.refresh_all)
    mana_deleF.delok.clicked.connect(mana_f.refresh_all)
    mana_reF.reok.clicked.connect(mana_f.refresh_all)
    # 管理员管理机票
    mana_reT.reok.clicked.connect(mana_t.refresh_all)
    # 管理员管理订单
    mana_reO.reok.clicked.connect(mana_o.refresh_all)
    mana_aO.reok.clicked.connect(mana_o.refresh_all)
    mana_deleO.delok.clicked.connect(mana_o.refresh_all)

    # 用户更改信息
    user_cinfo.reok.clicked.connect(user_info.refreshall)

    ui.show()
    sys.exit(app.exec_())

    conn.close()
