import wx
import pandas as pd
import wx.html2
import wx.html
import wx.lib.agw.hyperlink as hl
import folium
from folium.features import DivIcon
import os


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Plan Your Trip in Dublin!", size=(1100, 550))
        # self.panel = wx.Panel(self, wx.ID_ANY, size=(1100, 550))
        # self.panel.SetBackgroundColour("Blue")
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        panel = wx.Panel(self, size=(350, 40), pos=(20, 10))
        # panel.SetBackgroundColour(wx.Colour(0, 128,128))

        staticText1 = wx.StaticText(panel, -1, " Choose your current bus station:")
        sizer.Add(staticText1, 0, wx.ALL)

        stations = pd.read_csv('bus_stop.csv')
        stations = stations['stop_code'].unique()
        stations = [str(s) for s in stations]
        self.station_to_attraction = pd.read_csv('station_to_atraction.csv')
        self.attraction_station = pd.read_csv('attraction&station.csv')
        self.first_s, self.first_a, self.second_a, self.third_a = None, None, None, None

        self.combo_box_product = wx.ComboBox(panel, wx.ID_ANY, choices=stations,
                                             style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_COMBOBOX, self.OnCombo, self.combo_box_product)

        sizer.Add(self.combo_box_product, 0, wx.ALL, 10)
        button = wx.Button(panel, -1, "Select")
        button.SetBackgroundColour((255, 230, 200, 255))
        self.Bind(wx.EVT_BUTTON, self.func, button)
        sizer.Add(button, 0, wx.ALL, 10)

        # set image
        panel = wx.Panel(self, size=(550, 220), pos=(550, 10))
        sizer1 = wx.GridBagSizer(5, 5)
        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('welcome_dublin.png'))
        sizer1.Add(icon, pos=(0, 4), flag=wx.TOP | wx.RIGHT | wx.ALIGN_RIGHT,
                   border=5)

        self.SetSizer(sizer)
        self.Show()

    def OnCombo(self, event):
        product = self.combo_box_product.GetValue()
        return product

    def OnCombo2(self, event):
        product = self.combo_box_product.GetValue()
        return product

    def OnCombo3(self, event):
        product = self.combo_box_product.GetValue()
        return product

    def OnCombo4(self, event):
        product = self.combo_box_product.GetValue()
        return product

    def func(self, event):
        # panel = wx.Panel(self, size=(750, 40), pos=(20, 70))
        x = self.OnCombo(None)
        print(x)
        self.first_s = int(x)
        att = self.station_to_attraction[self.station_to_attraction['station'] == int(x)]['attraction'].values
        att = list(att)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        staticText1 = wx.StaticText(self, -1, " Choose your first attraction:", pos=(20, 60))
        sizer.Add(staticText1, 0, wx.ALL)
        self.combo_box_product = wx.ComboBox(self, wx.ID_ANY, choices=att, pos=(20, 80),
                                             style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_COMBOBOX, self.OnCombo2, self.combo_box_product)
        sizer.Add(self.combo_box_product, 0, wx.ALL, 10)
        button = wx.Button(self, -1, "Select", pos=(470, 80))
        button.SetBackgroundColour((255, 230, 200, 255))
        self.Bind(wx.EVT_BUTTON, self.func2, button)
        sizer.Add(button, 0, wx.ALL, 10)

    def func2(self, event):
        x = self.OnCombo2(None)
        print(x)
        self.first_a = x
        stations = self.attraction_station[self.attraction_station['attraction'] == x]['bus_stations'].values[0].strip(
            '[').strip(']').split(',')
        int_stations = list()
        for idx, s in enumerate(stations):
            if idx == 0:
                int_stations.append(int(s))
            else:
                int_stations.append(int(s[1:]))
        self.second_s = int_stations
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        staticText1 = wx.StaticText(self, -1, " Choose your second attraction:", pos=(20, 110))
        sizer.Add(staticText1, 0, wx.ALL)

        att = self.station_to_attraction[self.station_to_attraction['station'].isin(int_stations)]['attraction'].values

        att = list(att)
        self.combo_box_product = wx.ComboBox(self, wx.ID_ANY, choices=att, pos=(20, 130),
                                             style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_COMBOBOX, self.OnCombo3, self.combo_box_product)
        sizer.Add(self.combo_box_product, 0, wx.ALL, 10)
        button = wx.Button(self, -1, "Select", pos=(470, 130))
        button.SetBackgroundColour((255, 230, 200, 255))
        self.Bind(wx.EVT_BUTTON, self.func3, button)
        sizer.Add(button, 0, wx.ALL, 10)

    def func3(self, event):
        x = self.OnCombo3(None)
        print(x)
        self.second_a = x
        stations = self.attraction_station[self.attraction_station['attraction'] == x]['bus_stations'].values[0].strip(
            '[').strip(']').split(',')
        int_stations = list()
        for idx, s in enumerate(stations):
            if idx == 0:
                int_stations.append(int(s))
            else:
                int_stations.append(int(s[1:]))

        print(stations)
        self.third_s = int_stations
        att = self.station_to_attraction[self.station_to_attraction['station'].isin(int_stations)]['attraction'].values

        att = list(att)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        staticText1 = wx.StaticText(self, -1, " Choose your third attraction:", pos=(20, 160))
        sizer.Add(staticText1, 0, wx.ALL)

        self.combo_box_product = wx.ComboBox(self, wx.ID_ANY, choices=att, pos=(20, 180),
                                             style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_COMBOBOX, self.OnCombo, self.combo_box_product)
        sizer.Add(self.combo_box_product, 0, wx.ALL, 10)
        button = wx.Button(self, -1, "Select", pos=(470, 180))
        button.SetBackgroundColour((255, 230, 200, 255))
        self.Bind(wx.EVT_BUTTON, self.func4, button)
        sizer.Add(button, 0, wx.ALL, 10)

    def func4(self, event):
        x = self.OnCombo4(None)
        print(x)
        self.third_a = x
        self.final_output()

    def final_output(self):
        self.create_map()
        first_lines = self.station_to_attraction[(self.station_to_attraction['attraction'] == self.first_a) & (
                self.station_to_attraction['station'] == self.first_s)]['lines'].values[0]
        first_lines = first_lines.strip('[').strip(']').strip("'").replace("'", "").split(', ')
        lines = ''
        for idx, item in enumerate(first_lines):
            for idx2, item2 in enumerate(item):
                if (idx2 < 2 and item2 == '0') or idx2 == 4:
                    continue
                lines += item2
            if idx != len(first_lines) - 1:
                lines += ', '
        print(first_lines,lines)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        att = pd.read_csv('attraction.csv')
        phone = att[att['Name'] == self.first_a]['Telephone'].values[0]
        url = att[att['Name'] == self.first_a]['Url'].values[0]
        if phone and url:
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the first attraction are: {lines}\n for more inforamtion you can contect {phone}\n and visit {url}",
                                        pos=(20, 220))
        elif phone and not url:
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the first attraction are: {first_lines}\n for more inforamtion you can contect {phone}",
                                        pos=(20, 220))
        else:
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the first attraction are: {first_lines}\n",
                                        pos=(20, 220))
        sizer.Add(staticText1, 0, wx.ALL)

        second_lines = self.station_to_attraction[(self.station_to_attraction['attraction'] == self.second_a) & (
            self.station_to_attraction['station'].isin(self.second_s))]['lines'].values[0]
        second_lines = second_lines.strip('[').strip(']').strip("'").strip('"').strip('`').replace("'", "").split(', ')
        lines = ''
        for idx, item in enumerate(first_lines):
            for idx2, item2 in enumerate(item):
                if (idx2 < 2 and item2 == '0') or idx2 == 4:
                    continue
                lines += item2
            if idx != len(first_lines) - 1:
                lines += ', '
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        phone = att[att['Name'] == self.second_a]['Telephone'].values[0]
        url = att[att['Name'] == self.second_a]['Url'].values[0]
        if phone and url:
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the second attraction are: {lines}\n for more inforamtion you can contect {phone}\n and visit {url}",
                                        pos=(20, 280))
        elif phone and not url:
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the second attraction are: {second_lines}\n for more inforamtion you can contect {phone}",
                                        pos=(20, 280))
        else:
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the second attraction are: {second_lines}\n",
                                        pos=(20, 280))
        sizer.Add(staticText1, 0, wx.ALL)

        third_lines = self.station_to_attraction[(self.station_to_attraction['attraction'] == self.second_a) & (
            self.station_to_attraction['station'].isin(self.third_s))]['lines'].values[0]
        third_lines = third_lines.strip('[').strip(']').strip("'").strip('"').strip('`').replace("'", "").split(', ')
        lines = ''
        for idx, item in enumerate(first_lines):
            for idx2, item2 in enumerate(item):
                if (idx2 < 2 and item2 == '0') or idx2 == 4:
                    continue
                lines += item2
            if idx != len(first_lines) - 1:
                lines += ', '
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        phone = att[att['Name'] == self.third_a]['Telephone'].values[0]
        url = att[att['Name'] == self.third_a]['Url'].values[0]
        if phone and url:
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the third attraction are: {lines}\n for more inforamtion you can contect {phone}\n and visit {url}",
                                        pos=(20, 340))
        elif phone and not url:
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the third attraction are: {third_lines}\n for more inforamtion you can contect {phone}",
                                        pos=(20, 340))
        else:
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the third attraction are: {third_lines}\n",
                                        pos=(20, 340))
        sizer.Add(staticText1, 0, wx.ALL)

        # set image
        panel = wx.Panel(self, size=(500, 300), pos=(600, 250))
        sizer1 = wx.GridBagSizer(5, 5)
        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('dublin_safe.png'))
        sizer1.Add(icon, pos=(0, 4), flag=wx.TOP | wx.RIGHT | wx.ALIGN_RIGHT,
                   border=5)

        # set hyperlink to map
        hl.HyperLinkCtrl(self, -1, 'To see on map click here', URL="https://epic-lumiere-c21f13.netlify.app/",
                         pos=(20, 400), size=(140, 20))

    def create_map(self):
        att = pd.read_csv('attraction.csv')
        stops = pd.read_csv('bus_stop.csv')

        s_lat = stops[stops['stop_code'] == self.first_s]['Y'].values[0]
        s_long = stops[stops['stop_code'] == self.first_s]['X'].values[0]

        at1_lat = att[att['Name'] == self.first_a]['Latitude'].values[0]
        at1_long = att[att['Name'] == self.first_a]['Longitude'].values[0]
        at2_lat = att[att['Name'] == self.second_a]['Latitude'].values[0]
        at2_long = att[att['Name'] == self.second_a]['Longitude'].values[0]
        at3_lat = att[att['Name'] == self.third_a]['Latitude'].values[0]
        at3_long = att[att['Name'] == self.third_a]['Longitude'].values[0]


        d = {'long': [at1_long, at2_long, at3_long], 'lat': [at1_lat, at2_lat, at3_lat],
             'name': ['Attraction 1', 'Attraction 2', 'Attraction 3']}
        df_loc = pd.DataFrame(data=d)

        map_osm = folium.Map(location=[df_loc.iloc[0]["lat"], df_loc.iloc[0]["long"]], zoom_start=12)

        folium.Marker(location=[s_lat, s_long],
                      icon=folium.Icon(color='red', icon='info-sign')).add_to(
            map_osm)

        df_loc.apply(
            lambda row: folium.Marker(location=[row["lat"], row["long"]],
                                      icon=folium.Icon(color='blue', icon='info-sign')).add_to(
                map_osm),
            axis=1)
        folium.Marker((s_lat, s_long + 0.001), icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(7, 20),
            html='<div style="font-size: 11pt; color : red; font-weight:bold; background:white; opacity:0.75;border:2px solid black;">you are here</div>',
        )).add_to(map_osm)
        folium.Marker((at1_lat, at1_long + 0.001), icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(7, 20),
            html=f'<div style="font-size: 11pt; color : black;font-weight:bold;background:white;opacity:0.75;border:2px solid black;">{self.first_a}</div>',
        )).add_to(map_osm)
        folium.Marker((at2_lat, at2_long + 0.001), icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(7, 20),
            html=f'<div style="font-size: 11pt; color : black;font-weight:bold;background:white;opacity:0.75;border:2px solid black;">{self.second_a}</div>',
        )).add_to(map_osm)
        folium.Marker((at3_lat, at3_long + 0.001), icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(7, 20),
            html=f'<div style="font-size: 11pt; color : black;font-weight:bold;background:white;opacity:0.75;border:2px solid black;">{self.third_a}</div>',
        )).add_to(map_osm)

        map_osm.save("index.html")
        os.system('git add index.html')
        os.system('git commit -m "update"')
        os.system('git push')


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
