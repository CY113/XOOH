# coding=utf-8

import scrapy


class board_details_item(scrapy.Item):
    id = scrapy.Field()
    sn = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    price_discount = scrapy.Field()
    price_dealer = scrapy.Field()
    cover = scrapy.Field()
    import_cover_name = scrapy.Field()
    import_video_name = scrapy.Field()
    video = scrapy.Field()
    city = scrapy.Field()
    district = scrapy.Field()
    town = scrapy.Field()
    bmap_resolved = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    address = scrapy.Field()
    orientation_intro = scrapy.Field()
    wight = scrapy.Field()
    hight = scrapy.Field()
    show_wight = scrapy.Field()
    show_hight = scrapy.Field()
    floor_hight = scrapy.Field()
    type = scrapy.Field()
    show_type = scrapy.Field()
    begin_show_time = scrapy.Field()
    end_show_time = scrapy.Field()
    show_time_text = scrapy.Field()
    ferer_time = scrapy.Field()
    show_times = scrapy.Field()
    show_times_people = scrapy.Field()
    show_times_car = scrapy.Field()
    sound_intro = scrapy.Field()
    around_intro = scrapy.Field()
    min_buy_time = scrapy.Field()
    confirm_time = scrapy.Field()
    complete_time = scrapy.Field()
    intro = scrapy.Field()
    keyword = scrapy.Field()
    position_point = scrapy.Field()
    use_trade = scrapy.Field()
    total_point = scrapy.Field()
    comment_point = scrapy.Field()
    ctime = scrapy.Field()
    mtime = scrapy.Field()
    option_user = scrapy.Field()
    last_option_user = scrapy.Field()
    company_id = scrapy.Field()
    company = scrapy.Field()
    server_name = scrapy.Field()
    company_intro = scrapy.Field()
    server_phone = scrapy.Field()
    trade_type = scrapy.Field()
    is_recomm = scrapy.Field()
    is_deleted = scrapy.Field()
    pre_sn = scrapy.Field()
    dimension = scrapy.Field()
    display_area = scrapy.Field()
    source_type = scrapy.Field()
    screens = scrapy.Field()
    remarks = scrapy.Field()
    prohibition = scrapy.Field()
    material = scrapy.Field()
    points = scrapy.Field()
    ground_clearance = scrapy.Field()
    lamplight = scrapy.Field()
    process_cost = scrapy.Field()
    point_chosemore = scrapy.Field()
    points_min = scrapy.Field()
    disable_decision = scrapy.Field()
    status = scrapy.Field()
    orientation = scrapy.Field()
    size_type = scrapy.Field()
    orientation_text = scrapy.Field()
    type_text = scrapy.Field()
    show_type_text = scrapy.Field()
    favorite = scrapy.Field()
    trades = scrapy.Field()
    _show_time = scrapy.Field()
    errno = scrapy.Field()
    errmsg = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """insert into board_details(id,sn,name,price,price_discount,price_dealer,cover,import_cover_name,import_video_name,video,city,district,town,bmap_resolved,longitude,latitude,address,orientation_intro,wight,hight,show_wight,show_hight,floor_hight,type,show_type,begin_show_time,end_show_time,show_time_text,ferer_time,show_times,show_times_people,show_times_car,sound_intro,around_intro,min_buy_time,confirm_time,complete_time,intro,keyword,position_point,use_trade,total_point,comment_point,ctime,mtime,option_user,last_option_user,company_id,company,server_name,company_intro,server_phone,trade_type,is_recomm,is_deleted,pre_sn,dimension,display_area,source_type,screens,remarks,prohibition,material,points,ground_clearance,lamplight,process_cost,point_chosemore,points_min,disable_decision,status,orientation,size_type,orientation_text,type_text,show_type_text,favorite,trades,_show_time,errno,errmsg) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        params = (self["id"], self["sn"], self["name"], self["price"],
                  self["price_discount"], self["price_dealer"],
                  self["cover"], self["import_cover_name"],
                  self["import_video_name"], self["video"], self["city"],
                  self["district"], self["town"], self["bmap_resolved"],
                  self["longitude"], self["latitude"], self["address"],
                  self["orientation_intro"], self["wight"], self["hight"],
                  self["show_wight"], self["show_hight"], self["floor_hight"],
                  self["type"], self["show_type"], self["begin_show_time"],
                  self["end_show_time"], self["show_time_text"],
                  self["ferer_time"], self["show_times"], self["show_times_people"],
                  self["show_times_car"], self["sound_intro"],
                  self["around_intro"], self["min_buy_time"],
                  self["confirm_time"], self["complete_time"], self["intro"],
                  self["keyword"], self["position_point"], self["use_trade"],
                  self["total_point"], self["comment_point"], self["ctime"],
                  self["mtime"], self["option_user"], self["last_option_user"],
                  self["company_id"], self["company"], self["server_name"],
                  self["company_intro"], self["server_phone"],
                  self["trade_type"], self["is_recomm"], self["is_deleted"],
                  self["pre_sn"], self["dimension"], self["display_area"],
                  self["source_type"], self["screens"], self["remarks"],
                  self["prohibition"], self["material"], self["points"],
                  self["ground_clearance"], self["lamplight"],
                  self["process_cost"], self["point_chosemore"],
                  self["points_min"], self["disable_decision"], self["status"],
                  self["orientation"], self["size_type"],
                  self["orientation_text"], self["type_text"],
                  self["show_type_text"], self["favorite"], self["trades"],
                  self["_show_time"], self["errno"], self["errmsg"])
        return insert_sql, params

    def distinct_data(self):
        query = """select sn from board_details where sn =%s"""
        params = (self["sn"])
        return query, params


"""
    id,sn,name,price,price_discount,price_dealer,cover,import_cover_name,import_video_name,video,city,district,town,bmap_resolved,longitude,latitude,address,orientation_intro,wight,hight,show_wight,show_hight,floor_hight,type,show_type,begin_show_time,end_show_time,show_time_text,ferer_time,show_times,show_times_people,show_times_car,sound_intro,around_intro,min_buy_time,confirm_time,complete_time,intro,keyword,position_point,use_trade,total_point,comment_point,ctime,mtime,option_user,last_option_user,company_id,company,server_name,company_intro,server_phone,trade_type,is_recomm,is_deleted,pre_sn,dimension,display_area,source_type,screens,remarks,prohibition,material,points,ground_clearance,lamplight,process_cost,point_chosemore,points_min,disable_decision,status,orientation,size_type,orientation_text,type_text,show_type_text,favorite,trades,_show_time,errno,errmsg,


















"""
