from toolbox import update_ui
from toolbox import CatchException, report_exception
from toolbox import write_history_to_file, promote_file_to_downloadzone
from .crazy_utils import request_gpt_model_in_new_thread_with_ui_alive

fast_debug = False


@CatchException
def 解析Python项目(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, user_request):
    history = []  # 清空历史，以免输入溢出
    import glob, os
    if os.path.exists(txt):
        project_folder = txt
    else:
        if txt == "": txt = '空空如也的输入栏'
        report_exception(chatbot, history, a=f"解析项目: {txt}", b=f"找不到本地项目或无权访问: {txt}")
        yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面
        return
    file_manifest = [f for f in glob.glob(f'{project_folder}/**/*.py', recursive=True)]
    print(file_manifest)

    if len(file_manifest) == 0:
        report_exception(chatbot, history, a=f"解析项目: {txt}", b=f"找不到任何python文件: {txt}")
        yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面
        return
    # yield from 解析源代码新(file_manifest, project_folder, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt)
