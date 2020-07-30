from poium import Page, PageElement, PageElements,NewPageElement


class BaiduPage(Page):
    search_input = PageElement(id_="kw", describe="搜索框")
    search_button = PageElement(id_="su", describe="搜索按钮")
    settings = PageElement(link_text="设置", describe="设置下拉框")
    # settings = NewPageElement(id_='s-usersetting-top',describe="设置下拉框")#此行有效，可测试通过；如果想看测试不通过的结果，用上面那个语句。
    search_setting = PageElement(css=".setpref", describe="搜索设置选项")#下面这行的方法也可以。
    # search_setting = NewPageElement(link_text='搜索设置', describe="搜索设置选项")
    save_setting = PageElement(css=".prefpanelgo", describe="保存设置")

    # 定位一组元素
    search_result = PageElements(xpath="//div/h3/a", describe="搜索结果")
