import justpy as jp


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="lHh lpr fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)



        drawer = jp.QDrawer(a=layout, show_if_above=True, v_model="left", border=True)
        jp.QBtn(a=toolbar, dence=True, flat=True, round=True, icon="menu", click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
               Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec turpis nulla,
               lobortis non diam pulvinar, egestas rhoncus eros. Etiam faucibus feugiat felis,
               vitae faucibus sem laoreet eget. Praesent sit amet orci sed lacus commodo aliquam
               id iaculis augue. Aliquam ac lacus nec massa cursus tincidunt sed vitae ex.
               Vestibulum eros est, tincidunt vitae mauris vitae, interdum ullamcorper libero. 
               Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis 
               egestas. Cras varius nulla id lorem feugiat laoreet. Suspendisse est massa,
               accumsan quis nisi vitae, blandit accumsan turpis. Vivamus finibus leo
               consectetur urna imperdiet pulvinar. Nulla sollicitudin lacus nec dui accumsan,
               sed dignissim mauris maximus.
               """, classes="text-lg")
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value == True:
            widget.drawer.value = False
        else:
            widget.drawer.value = True