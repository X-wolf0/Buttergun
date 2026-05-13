import time
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
}

for start in range(1, 2):
    url_page = f"http://111.115.201.16/problem.php?page={start}"
    time.sleep(1)
    res_1 = requests.get(url_page, headers=headers)
    res_1.encoding = "utf-8"
    soup_1 = BeautifulSoup(res_1.text, "html.parser")

    for id_ in range(1000, 2494):
        url_id = f"http://111.115.201.16/problem.php?id={id_}"
        time.sleep(1)
        res_2 = requests.get(url_id, headers=headers)
        res_2.encoding = "utf-8"
        soup_2 = BeautifulSoup(res_2.text, "html.parser")

        card_body = soup_2.find("div", attrs = {"class" : "card-body"})

        h3_tag = card_body.find("h3")
        if h3_tag:
            print(h3_tag.get_text().strip())

        start_tag = None
        for h4 in soup_2.find_all("h4"):
            if "Description" in h4.get_text(strip=True):
                start_tag = h4
                break

        desc_content = []

        # 如果找到了开始标签，就往下遍历同级标签
        if start_tag:
            # 从下一个同级标签开始
            current_tag = start_tag.find_next_sibling()

            # 循环提取，直到遇到【停止标签】：包含“输入”的标签
            while current_tag:
                # 判断：遇到停止标记就结束
                if "输入" in current_tag.get_text(strip=True):
                    break

                # 提取当前标签的所有文本
                text = current_tag.get_text(strip=True)
                if text:
                    desc_content.append(text)

                # 继续取下一个同级标签
                current_tag = current_tag.find_next_sibling()

        # 输出结果
        if desc_content:
            print("题目描述：")
            print("".join(desc_content))
        else:
            print("题目描述：无内容")

#---------------------------------------------------------------------
        start_Input_tag = None
        for h4 in soup_2.find_all("h4"):
            if "Input" in h4.get_text(strip=True):
                start_Input_tag = h4
                break

        desc_content_Input = []
        # 如果找到了开始标签，就往下遍历同级标签
        if start_Input_tag:
            # 从下一个同级标签开始
            current_tag_Input = start_Input_tag.find_next_sibling()

            # 循环提取，直到遇到【停止标签】：包含“输入”的标签
            while current_tag_Input:
                # 判断：遇到停止标记就结束
                if "Input" in current_tag_Input.get_text(strip=True):
                    break

                # 提取当前标签的所有文本
                text_Input = current_tag_Input.get_text(strip=True)
                if text_Input:
                    desc_content_Input.append(text_Input)

                # 继续取下一个同级标签
                current_tag_Input = current_tag_Input.find_next_sibling()

        # 输出结果
        if desc_content_Input:
            print("输入：")
            print("".join(desc_content_Input))
        else:
            print("输入：无内容")

# ---------------------------------------------------------------------
        start_Output_tag = None
        for h4 in soup_2.find_all("h4"):
            if "Output" in h4.get_text(strip=True):
                start_Output_tag = h4
                break

        desc_content_Output = []
        # 如果找到了开始标签，就往下遍历同级标签
        if start_Output_tag:
            # 从下一个同级标签开始
            current_tag_Output = start_Output_tag.find_next_sibling()

            # 循环提取，直到遇到【停止标签】：包含“输入”的标签
            while current_tag_Output:
                # 判断：遇到停止标记就结束
                if "Output" in current_tag_Output.get_text(strip=True):
                    break

                # 提取当前标签的所有文本
                text_Output = current_tag_Output.get_text(strip=True)
                if text_Output:
                    desc_content_Output.append(text_Output)

                # 继续取下一个同级标签
                current_tag_Output = current_tag_Output.find_next_sibling()

        # 输出结果
        if desc_content_Output:
            print("输出：")
            print("".join(desc_content_Output))
        else:
            print("输出：无内容")

# ---------------------------------------------------------------------
        start_SampleInput_tag = None
        for h4 in soup_2.find_all("h4"):
            if "Sample Input" in h4.get_text(strip=True):
                start_SampleInput_tag = h4
                break

        desc_content_SampleInput = []
        # 如果找到了开始标签，就往下遍历同级标签
        if start_SampleInput_tag:
            # 从下一个同级标签开始
            current_tag_SampleInput = start_SampleInput_tag.find_next_sibling()

            # 循环提取，直到遇到【停止标签】：包含“输入”的标签
            while current_tag_SampleInput:
                # 判断：遇到停止标记就结束
                if "Sample Input" in current_tag_SampleInput.get_text(strip=True):
                    break

                # 提取当前标签的所有文本
                text_SampleInput = current_tag_SampleInput.get_text(strip=True)
                if text_SampleInput:
                    desc_content_SampleInput.append(text_SampleInput)

                # 继续取下一个同级标签
                current_tag_SampleInput = current_tag_SampleInput.find_next_sibling()

        # 输出结果
        if desc_content_SampleInput:
            print("样例输入：")
            print("".join(desc_content_SampleInput))
        else:
            print("输入：无内容")

# ---------------------------------------------------------------------
        start_SampleOutput_tag = None
        for h4 in soup_2.find_all("h4"):
            if "Sample Output" in h4.get_text(strip=True):
                start_SampleOutput_tag = h4
                break

        desc_content_SampleOutput = []
        # 如果找到了开始标签，就往下遍历同级标签
        if start_SampleOutput_tag:
            # 从下一个同级标签开始
            current_tag_SampleOutput = start_SampleOutput_tag.find_next_sibling()

            # 循环提取，直到遇到【停止标签】：包含“输入”的标签
            while current_tag_SampleOutput:
                # 判断：遇到停止标记就结束
                if "Sample Output" in current_tag_SampleOutput.get_text(strip=True):
                    break

                # 提取当前标签的所有文本
                text_SampleOutput = current_tag_SampleOutput.get_text(strip=True)
                if text_SampleOutput:
                    desc_content_SampleOutput.append(text_SampleOutput)

                # 继续取下一个同级标签
                current_tag_SampleOutput = current_tag_SampleOutput.find_next_sibling()

        # 输出结果
        if desc_content_SampleOutput:
            print("样例输出：")
            print("".join(desc_content_SampleOutput))
        else:
            print("输出：无内容")

# ---------------------------------------------------------------------
        start_Source_tag = None
        for h4 in soup_2.find_all("h4"):
            if "Source" in h4.get_text(strip=True):
                start_Source_tag = h4
                break

        desc_content_Source = []
        # 如果找到了开始标签，就往下遍历同级标签
        if start_Source_tag:
            # 从下一个同级标签开始
            current_tag_Source = start_Source_tag.find_next_sibling()

            # 循环提取，直到遇到【停止标签】：包含“输入”的标签
            while current_tag_Source:
                # 判断：遇到停止标记就结束
                if "Source" in current_tag_Source.get_text(strip=True):
                    break

                # 提取当前标签的所有文本
                text_Source = current_tag_Source.get_text(strip=True)
                if text_Source:
                    desc_content_Source.append(text_Source)

                # 继续取下一个同级标签
                current_tag_Source = current_tag_Source.find_next_sibling()

        # 输出结果
        if desc_content_Source:
            print("来源：")
            print("".join(desc_content_Source))
        else:
            print("来源：无内容")

# ---------------------------------------------------------------------
        start_limit_tag = None
        for h4 in soup_2.find_all("h4"):
            if "问题信息" in h4.get_text(strip=True):
                start_limit_tag = h4
                break

        desc_content_limit = []
        # 如果找到了开始标签，就往下遍历同级标签
        if start_limit_tag:
            # 从下一个同级标签开始
            current_tag_limit = start_limit_tag.find_next_sibling()

            # 循环提取，直到遇到【停止标签】：包含“输入”的标签
            while current_tag_limit:
                # 判断：遇到停止标记就结束
                if "问题信息" in current_tag_limit.get_text(strip=True):
                    break

                # 提取当前标签的所有文本
                text_limit = current_tag_limit.get_text(strip=True)
                if text_limit:
                    desc_content_limit.append(text_limit)

                # 继续取下一个同级标签
                current_tag_limit = current_tag_limit.find_next_sibling()

        # 输出结果
        if desc_content_limit:
            print("文件限制：")
            print("".join(desc_content_limit))
            print("\n")
        else:
            print("文件限制：无内容")