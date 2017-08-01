import os
import qd.Constant


def request_class(perfix, cmd):
    req_path = qd.Constant.PROJECT + qd.Constant.PACKAGE + qd.Constant.REQUEST
    req_class_name = perfix + 'ReqBean'
    req_file_name = req_class_name + '.java'
    hasfile = check_file(req_path, req_file_name)
    if hasfile is False:
        code = genReqCode(req_class_name, cmd)
        write_file(req_path, req_file_name, req_class_name, code)


def response_class(perfix, cmd):
    res_path = qd.Constant.PROJECT + qd.Constant.PACKAGE + qd.Constant.RESPONSE
    res_class_name = perfix + 'ResBean'
    res_file_name = res_class_name + '.java'
    hasfile = check_file(res_path, res_file_name)
    if hasfile is False:
        code = genResCode(res_class_name)
        write_file(res_path, res_file_name, res_class_name, code)


def write_file(req_path, req_file_name, req_class_name, code):
    print('写入文件..')
    os.chdir(req_path)
    os.mknod(req_file_name)
    file = open(req_file_name, 'w')
    file.write(code)
    file.close()


def check_file(path, filename):
    reqfilelist = os.listdir(path)
    # Mall.Pay
    for i in range(0, len(reqfilelist)):
        if reqfilelist[i] == filename:
            print('文件已存在，不作任何操作。')
            return True
    return False


def genReqCode(class_name, cmd):
    code = 'package com.wefax.wallete.bean.request;\n\n'
    code += 'import com.wefax.wallete.bean.request.commn.CMD_Request;\n'
    code += 'import com.wefax.wallete.util.CMDConstant;\n\n'
    code += 'public class ' + class_name + ' extends CMD_Request {\n'
    code += '    @Override\n'
    code += '    public String[] getArgs() {\n'
    code += '        return CMDConstant.' + cmd + ';\n'
    code += '    }\n'
    code += '}'
    return code


def genResCode(class_name):
    code = 'package com.wefax.wallete.bean.response;\n\n'
    code += 'public class ' + class_name + ' {\n\n'
    code += '}'
    return code


def check_input(cmd):
    list = []
    list = cmd.split('.')
    perfix = ''
    for i in range(0, len(list)):
        perfix += list[i] + '_'
    request_class(perfix, cmd)
    response_class(perfix, cmd)
