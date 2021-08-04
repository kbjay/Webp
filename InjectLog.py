# encoding: utf-8
import os


class ParserError(Exception):
    pass


# 注入代码到一个函数块中
def inject_code_to_method_section(method_section):
    # 静态构造函数，无需处理
    if method_section[0].find("static constructor") != -1:
        return method_section
    # synthetic函数，无需处理
    if method_section[0].find("synthetic") != -1:
        return method_section
    # 抽象方法，无需处理
    if method_section[0].find("abstract") != -1:
        return method_section
    # 生成待插入代码行
    inject_code = [
        '\n',
        '    invoke-static {}, Lcom/kbjay/decompile/hook/log/InjectLog;->printFunc()V\n',
        '\n'
    ]
    # 插入到.prologue的下一行
    is_inject = False
    for i in range(0, len(method_section)):
        # if method_section[i].find(".prologue") != -1: (这里根据具体情况插入)
        if method_section[i].find(".locals") != -1:
            is_inject = True
            method_section[i + 1: i + 1] = inject_code
            break

    return method_section


def inject_log_code(content):
    new_content = []
    method_section = []
    is_method_begin = False
    for line in content:
        if line[:7] == ".method":
            is_method_begin = True
            method_section.append(line)
            continue
        if is_method_begin:
            method_section.append(line)
        else:
            new_content.append(line)
        if line[:11] == ".end method":
            if not is_method_begin:
                raise ParserError(".method不对称")
            is_method_begin = False
            new_method_section = inject_code_to_method_section(method_section)
            new_content.extend(new_method_section)
            del method_section[:]

    return new_content


def main():
    walker = os.walk("E:\Decompile\\apktool\smali\eu\\tsoml\graphicssettings")
    for root, directory, files in walker:
        for file_name in files:
            if file_name[-6:] != ".smali":
                continue
            file_path = root + "/" + file_name
            print(file_path)
            file = open(file_path)
            lines = file.readlines()
            file.close()
            new_code = inject_log_code(lines)
            file = open(file_path, "w")
            file.writelines(new_code)
            file.close()


if __name__ == '__main__':
    main()