import wx
import pandas as pd
import wx.html2
import wx.html
import wx.lib.agw.hyperlink as hl
import folium
from folium.features import DivIcon
import os
from geopy import distance
import shapefile
import ast
import math

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Plan Your Trip in Dublin!", size=(1100, 650))
        self.panel = wx.Panel(self,size=(350, 40), pos=(20, 10))
        panel = wx.Panel(self, size=(500, 40), pos=(20, 10))
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        staticText1 = wx.StaticText(self, -1, "Plan your trip in Dublin!",size=(500, 40), pos=(20, 10))
        staticText1.SetFont(wx.Font(26, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.FONTWEIGHT_BOLD, False, 'Ariel'))
        staticText1.SetForegroundColour('#1e67bd')
        sizer.Add(staticText1, 0, wx.ALL)
        # self.panel.SetBackgroundColour("Blue")
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        panel = wx.Panel(self, size=(370, 40), pos=(20, 60))
        # panel.SetBackgroundColour(wx.Colour(0, 128,128))

        staticText1 = wx.StaticText(panel, -1, " Choose your current bus station:")
        staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Ariel'))
        sizer.Add(staticText1, 0, wx.ALL)

        stations = pd.read_csv('data/bus_stop.csv')
        stations = stations['stop_code'].unique()
        stations = [str(s) for s in stations]
        self.station_to_attraction = pd.read_csv('data/station_to_attraction.csv')
        self.attraction_station = pd.read_csv('data/attraction&station.csv')
        self.first_s, self.first_a, self.second_a, self.third_a = None, None, None, None

        self.combo_box_product = wx.ComboBox(panel, wx.ID_ANY, choices=stations,
                                             style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_COMBOBOX, self.OnCombo, self.combo_box_product)

        sizer.Add(self.combo_box_product, 0, wx.ALL, 10)
        button = wx.Button(panel, -1, "Select")
        button.SetBackgroundColour('#7F9DC0')
        self.Bind(wx.EVT_BUTTON, self.func, button)
        sizer.Add(button, 0, wx.ALL, 10)

        # set image
        panel = wx.Panel(self, size=(512, 288), pos=(550, 10))
        sizer1 = wx.GridBagSizer(5, 5)
        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('data/dublin_guide_resized.jpg'))
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
        x = self.OnCombo(None)
        print(x)
        self.first_s = int(x)
        att = self.station_to_attraction[self.station_to_attraction['station'] == int(x)]['attraction'].values
        att = list(att)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        staticText1 = wx.StaticText(self, -1, " Choose your first attraction:", pos=(20, 110))
        staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Ariel'))
        sizer.Add(staticText1, 0, wx.ALL)
        self.combo_box_product = wx.ComboBox(self, wx.ID_ANY, choices=att, pos=(20, 130),size=(425, 40),
                                             style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_COMBOBOX, self.OnCombo2, self.combo_box_product)
        sizer.Add(self.combo_box_product, 0, wx.ALL, 10)
        button = wx.Button(self, -1, "Select", pos=(460, 130))
        button.SetBackgroundColour('#7F9DC0')
        self.Bind(wx.EVT_BUTTON, self.func2, button)
        sizer.Add(button, 0, wx.ALL, 10)

    def func2(self, event):
        x = self.OnCombo2(None)
        print(x)
        self.first_a = x
        stations = self.attraction_station[self.attraction_station['attraction'] == x]['bus_stations'].values[0].strip(
            '[').strip(']').split(', ')
        int_stations = list()
        for idx, s in enumerate(stations):
            int_stations.append(int(s))
        print(int_stations)
        self.second_s = int_stations
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        staticText1 = wx.StaticText(self, -1, " Choose your second attraction:", pos=(20, 160))
        staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Ariel'))
        sizer.Add(staticText1, 0, wx.ALL)

        att = self.station_to_attraction[self.station_to_attraction['station'].isin(int_stations)]['attraction'].values

        att = list(att)
        self.combo_box_product = wx.ComboBox(self, wx.ID_ANY, choices=att, pos=(20, 180),size=(425, 40),
                                             style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_COMBOBOX, self.OnCombo3, self.combo_box_product)
        sizer.Add(self.combo_box_product, 0, wx.ALL, 10)
        button = wx.Button(self, -1, "Select", pos=(460, 180))
        button.SetBackgroundColour('#7F9DC0')
        self.Bind(wx.EVT_BUTTON, self.func3, button)
        sizer.Add(button, 0, wx.ALL, 10)

    def func3(self, event):
        x = self.OnCombo3(None)
        print(x)
        self.second_a = x
        stations = self.attraction_station[self.attraction_station['attraction'] == x]['bus_stations'].values[0].strip(
            '[').strip(']').split(', ')
        int_stations = list()
        for idx, s in enumerate(stations):
            int_stations.append(int(s))

        print(int_stations)
        self.third_s = int_stations
        att = self.station_to_attraction[self.station_to_attraction['station'].isin(int_stations)]['attraction'].values

        att = list(att)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        staticText1 = wx.StaticText(self, -1, " Choose your third attraction:", pos=(20, 210))
        staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Ariel'))
        sizer.Add(staticText1, 0, wx.ALL)

        self.combo_box_product = wx.ComboBox(self, wx.ID_ANY, choices=att, pos=(20, 230),size=(425, 40),
                                             style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_COMBOBOX, self.OnCombo, self.combo_box_product)
        sizer.Add(self.combo_box_product, 0, wx.ALL, 10)
        button = wx.Button(self, -1, "Select", pos=(460, 230))
        button.SetBackgroundColour('#7F9DC0')
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
        first_lines = ast.literal_eval(first_lines)
        # first_lines = first_lines.strip('[').strip(']').strip("'").replace("'", "").split(', ')
        lines = ''
        for idx, item in enumerate(first_lines):
            item = item[:-1].upper()
            lines += item
            if idx != len(first_lines) - 1:
                lines += ', '
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        att = pd.read_csv('data/attraction.csv')
        phone = str(att[att['Name'] == self.first_a]['Telephone'].values[0])
        url = str(att[att['Name'] == self.first_a]['Url'].values[0])
        if phone != 'nan' and url != 'nan':
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the first attraction are: {lines}\nFor more inforamtion you can contect {phone}\nand visit {url}",
                                        pos=(20, 290))
        elif phone != 'nan' and url == 'nan':
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the first attraction are: {lines}\nFor more inforamtion you can contect {phone}",
                                        pos=(20, 290))
        else:
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the first attraction are: {lines}\n",
                                        pos=(20, 290))
        staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Calibri'))
        sizer.Add(staticText1, 0, wx.ALL)

        second_lines = self.station_to_attraction[(self.station_to_attraction['attraction'] == self.second_a) & (
            self.station_to_attraction['station'].isin(self.second_s))]['lines'].values[0]
        second_lines = ast.literal_eval(second_lines)
        lines = ''
        for idx, item in enumerate(second_lines):
            item = item[:-1].upper()
            lines += item
            if idx != len(second_lines) - 1:
                lines += ', '
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        phone = str(att[att['Name'] == self.second_a]['Telephone'].values[0])
        url = str(att[att['Name'] == self.second_a]['Url'].values[0])
        if phone != 'nan' and url != 'nan':
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the second attraction are: {lines}\nFor more inforamtion you can contect {phone}\nand visit {url}",
                                        pos=(20, 370))
        elif phone != 'nan' and url == 'nan':
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the second attraction are: {lines}\nFor more inforamtion you can contect {phone}",
                                        pos=(20, 370))
        else:
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the second attraction are: {lines}\n",
                                        pos=(20, 370))
        staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Calibri'))
        sizer.Add(staticText1, 0, wx.ALL)

        third_lines = self.station_to_attraction[(self.station_to_attraction['attraction'] == self.third_a) & (
            self.station_to_attraction['station'].isin(self.third_s))]['lines'].values[0]
        third_lines = ast.literal_eval(third_lines)
        lines = ''
        for idx, item in enumerate(third_lines):
            item = item[:-1].upper()
            lines += item
            if idx != len(third_lines) - 1:
                lines += ', '
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        phone = str(att[att['Name'] == self.third_a]['Telephone'].values[0])
        url = str(att[att['Name'] == self.third_a]['Url'].values[0])
        if phone != 'nan' and url != 'nan':
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the third attraction are: {lines}\nFor more inforamtion you can contect {phone}\nand visit {url}",
                                        pos=(20, 450))
        elif phone != 'nan' and url == 'nan':
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the third attraction are: {lines}\nFor more inforamtion you can contect {phone}",
                                        pos=(20, 450))
        else:
            staticText1 = wx.StaticText(self, -1,
                                        f"The needed lines for the third attraction are: {lines}\n",
                                        pos=(20, 450))
        staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False, 'Calibri'))
        sizer.Add(staticText1, 0, wx.ALL)

        # set image
        panel = wx.Panel(self, size=(480, 250), pos=(600, 320))
        sizer1 = wx.GridBagSizer(5, 5)
        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('data/dublin_safe.png'))
        sizer1.Add(icon, pos=(0, 4), flag=wx.TOP | wx.RIGHT | wx.ALIGN_RIGHT,
                   border=5)

        # set hyperlink to map
        hl.HyperLinkCtrl(self, -1, 'To see the locations on map click here', URL="https://epic-lumiere-c21f13.netlify.app/",
                         pos=(20, 540), size=(200, 20)).SetBold(Bold=True)


    def create_map(self):
        att = pd.read_csv('data/attraction.csv')
        stops = pd.read_csv('data/bus_stop.csv')

        s1_lat = stops[stops['stop_code'] == self.first_s]['Y'].values[0]
        s1_long = stops[stops['stop_code'] == self.first_s]['X'].values[0]
        s2_lat = stops[stops['stop_code'] == self.second_s[0]]['Y'].values[0]
        s2_long = stops[stops['stop_code'] == self.second_s[0]]['X'].values[0]
        s3_lat = stops[stops['stop_code'] == self.third_s[0]]['Y'].values[0]
        s3_long = stops[stops['stop_code'] == self.third_s[0]]['X'].values[0]

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


        folium.Marker(location=[s1_lat, s1_long],
                      icon=folium.Icon(icon='bus', prefix='fa',color='red')).add_to(
            map_osm)

        folium.Marker(location=[s2_lat, s2_long],
                      icon=folium.Icon(icon='bus', prefix='fa',color='purple'),tooltip=f'station to {self.second_a}').add_to(
            map_osm)
        folium.Marker(location=[s3_lat, s3_long],
                      icon=folium.Icon(icon='bus', prefix='fa',color='purple'),tooltip=f'station to {self.third_a}').add_to(
            map_osm)

        df_loc.apply(
            lambda row: folium.Marker(location=[row["lat"], row["long"]],
                                      icon=folium.Icon(color='blue', icon='info-sign')).add_to(
                map_osm),
            axis=1)


        ## add bus line
        possible_colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880',
                           '#FF97FF', '#FECB52']
        first_lines = self.station_to_attraction[(self.station_to_attraction['attraction'] == self.first_a) & (
                self.station_to_attraction['station'] == self.first_s)]['lines'].values[0]
        first_lines = ast.literal_eval(first_lines)
        # lines = ''
        for idx, item in enumerate(first_lines):
            item = item[:-1].upper()
            points = find_bus_route(item,(s1_lat,s1_long),(at1_lat,at1_long))
            if points:
                if len(possible_colors) == 0:
                    color = 'blue'
                else:
                    color = possible_colors[0]
                    del possible_colors[0]
                folium.vector_layers.PolyLine(points, color=color,tooltip=item).add_to(map_osm)

        second_lines = self.station_to_attraction[(self.station_to_attraction['attraction'] == self.second_a) & (
            self.station_to_attraction['station'] == self.second_s[0])]['lines'].values[0]
        second_lines = ast.literal_eval(second_lines)
        for idx, item in enumerate(second_lines):
            item = item[:-1].upper()
            points = find_bus_route(item, (s2_lat, s2_long), (at2_lat, at2_long))
            if points:
                if len(possible_colors) == 0:
                    color = 'blue'
                else:
                    color = possible_colors[0]
                    del possible_colors[0]
                folium.vector_layers.PolyLine(points, color=color,tooltip=item).add_to(map_osm)

        third_lines = self.station_to_attraction[(self.station_to_attraction['attraction'] == self.third_a) & (
                self.station_to_attraction['station'] == self.third_s[0])]['lines'].values[0]
        third_lines = ast.literal_eval(third_lines)
        for idx, item in enumerate(third_lines):
            item = item[:-1].upper()
            points = find_bus_route(item, (s3_lat, s3_long), (at3_lat, at3_long))
            if points:
                if len(possible_colors) == 0:
                    color = 'blue'
                else:
                    color = possible_colors[0]
                    del possible_colors[0]
                folium.vector_layers.PolyLine(points, color=color,tooltip=item).add_to(map_osm)

        # folium.Marker((s2_lat, s2_long + 0.001), icon=DivIcon(
        #     icon_size=(150, 36),
        #     icon_anchor=(7, 20),
        #     html='<div style="font-size: 11pt; color : red; font-weight:bold; background:white; opacity:0.75;border:2px solid black;">station to attraction 2</div>',
        # )).add_to(map_osm)
        #
        # folium.Marker((s3_lat, s3_long + 0.001), icon=DivIcon(
        #     icon_size=(150, 36),
        #     icon_anchor=(7, 20),
        #     html='<div style="font-size: 11pt; color : red; font-weight:bold; background:white; opacity:0.75;border:2px solid black;">station to attraction 3</div>',
        # )).add_to(map_osm)

        folium.Marker((s1_lat, s1_long + 0.001), icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(7, 20),
            html='<div style="font-size: 11pt; color : red; font-weight:bold; background:white; opacity:0.75;border:2px solid black;">you are here</div>',
        )).add_to(map_osm)
        folium.Marker((at1_lat, at1_long + 0.005), icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(7, 20),
            html=f'<div style="font-size: 11pt; color : black;font-weight:bold;background:white;opacity:0.75;border:2px solid black;"> 1 {self.first_a}</div>',
        )).add_to(map_osm)
        folium.Marker((at2_lat, at2_long + 0.005), icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(7, 20),
            html=f'<div style="font-size: 11pt; color : black;font-weight:bold;background:white;opacity:0.75;border:2px solid black;"> 2 {self.second_a}</div>',
        )).add_to(map_osm)
        folium.Marker((at3_lat, at3_long + 0.001), icon=DivIcon(
            icon_size=(150, 36),
            icon_anchor=(7, 20),
            html=f'<div style="font-size: 11pt; color : black;font-weight:bold;background:white;opacity:0.75;border:2px solid black;"> 3 {self.third_a}</div>',
        )).add_to(map_osm)

        map_osm.save("index.html")
        os.system('git add index.html')
        os.system('git commit -m "update"')
        os.system('git push')

def find_bus_route(bus_line,x_point,y_point):
    shape = shapefile.Reader("data/NTA_Public_Transport/NTA_Public_Transport.shp")
    shape_dict = {r.record.route_name: r.shape for r in shape.shapeRecords()}  # {lineid : Shape}
    if bus_line in shape_dict:
        parts = shape_dict[bus_line].parts
        points = shape_dict[bus_line].points
        geom = []
        for i in range(len(parts)):
            xy = []
            # pt = None
            if i < len(parts) - 1:
                pt = points[parts[i]:parts[i + 1]]
            else:
                pt = points[parts[i]:]
            for x, y in pt:
                xy.append([y, x])
            geom.append(xy)
        return update_route(x_point, y_point, geom)


def update_route(x,y,points): #x=(lat,long), y=(lat,long), points=[[(lat,long),(lat,long),..][..]]
    closest_to_x, closest_to_y = None,None
    min_dist_to_x, min_dist_to_y = None,None
    for row_idx, row in enumerate(points):
        for p_idx, p in enumerate(row):
            dist_x = distance.distance(x, p).m
            dist_y = distance.distance(y, p).m
            if not closest_to_x:
                closest_to_x, closest_to_y = (row_idx, p_idx), (row_idx, p_idx)
                min_dist_to_x, min_dist_to_y = dist_x, dist_y
            if min_dist_to_x > dist_x:
                closest_to_x = (row_idx, p_idx)
                min_dist_to_x = dist_x
            if min_dist_to_y > dist_y:
                closest_to_y = (row_idx, p_idx)
                min_dist_to_y = dist_y
    if closest_to_x == closest_to_y:
        closest_to_y = (closest_to_y[0],closest_to_y[1]+1)
    if closest_to_x[0] <= closest_to_y[0]:
        new_route = points[closest_to_x[0]:closest_to_y[0] + 1]
        new_route[0] = new_route[0][closest_to_x[1] - 1:]
        new_route[-1] = new_route[-1][:closest_to_y[1] + 1]
    else:
        new_route = points[closest_to_y[0]:closest_to_x[0] + 1]
        new_route[0] = new_route[0][closest_to_y[1] - 1:]
        new_route[-1] = new_route[-1][:closest_to_x[1] + 1]
    return new_route


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
