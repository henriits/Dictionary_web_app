import justpy as jp


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About page!", classes="text-4xl m-2")
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



