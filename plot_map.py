# import wx
# import wx.html2
#
# # class About(wx.Frame):
#     # def __init__(self):
#     #     wx.Panel.__init__(self,None,-1,title="Title",size=(700,700))
#
# class Test(wx.Frame):
#     def __init__(self,title,pos,size):
#         wx.Frame.__init__(self,None,-1,title,pos,size)
#         self.tester=wx.html2.WebView.New(self)
#         self.tester.LoadURL("https://moodle.technion.ac.il")
#
# if __name__ == "__main__":
#     app = wx.PySimpleApp()
#     frame = Test("html2 web view", (20, 20), (800, 600))
#     frame.Show()
#     app.MainLoop()
#

import os
import wx
import wx.html

FileFilter = "Html files (*.html)|*.html|" \
             "All files (*.*)|*.*"


class MyApp(wx.Frame):
    # ----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self,
                          None,
                          wx.ID_ANY,
                          "HTML Viewer with File picker"
                          )

        # Create a panel within the frame
        panel = wx.Panel(self, wx.ID_ANY)
        self.currentDirectory = os.getcwd()

        # Create the filepicker button and add the 'onOpenFile' binding
        openFileDlgBtn = wx.Button(
            panel,
            label="Choose an HTML File"
        )
        openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)

        # Put the button in a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(openFileDlgBtn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(sizer)

    # ----------------------------------------------------------------------

    """
        Create and show the Open FileDialog
    """

    def onOpenFile(self, event):
        dlg = wx.FileDialog(
            self,
            message="Choose a file",
            defaultDir=self.currentDirectory,
            defaultFile="",
            wildcard=FileFilter,
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR
        )

        ## If the user selects a file, open it in the Html File Viewer
        if dlg.ShowModal() == wx.ID_OK:
            htmlFilePath = dlg.GetPath()

            # Create a new instance of the HtmlViewer
            htmlViewerInstance = HtmlViewer(None, htmlFilePath)
            htmlViewerInstance.Show()

        dlg.Destroy()


# The HtmlViewer class expects the path of the HTML file
# to open it in a new window of the HtmlWindow type
class HtmlViewer(wx.Frame):
    def __init__(self, parent, filepath):
        wx.Frame.__init__(
            self,
            parent,
            -1,
            "HTML Viewer",
            size=(800, 600)
        )

        # Open a new HtmlWindow that is capable of rendering such content
        html = wx.html.HtmlWindow(self)
        self.Maximize(True)

        if "gtk2" in wx.PlatformInfo:
            html.SetStandardFonts()

            # Load the selected file in the viewer !
        html.LoadPage(filepath)


# Run the program !
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyApp()
    frame.Show()
    app.MainLoop()
