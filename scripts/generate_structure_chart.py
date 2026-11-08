import os
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False, serif=False):
    if serif:
        path = 'C:\\Windows\\Fonts\\timesbd.ttf' if bold else 'C:\\Windows\\Fonts\\times.ttf'
    else:
        path = 'C:\\Windows\\Fonts\\arialbd.ttf' if bold else 'C:\\Windows\\Fonts\\arial.ttf'
    
    if os.path.exists(path):
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()

def draw_box(draw, cx, cy, w, h, text, font, border_width=2, bg_fill='#ffffff', border_color='#000000', text_color='#000000'):
    x1, y1 = cx - w / 2, cy - h / 2
    x2, y2 = cx + w / 2, cy + h / 2
    draw.rectangle([x1, y1, x2, y2], fill=bg_fill, outline=border_color, width=border_width)
    
    lines = text.split('\n')
    line_h = []
    line_w = []
    for line in lines:
        bbox = font.getbbox(line)
        line_w.append(bbox[2] - bbox[0])
        line_h.append(bbox[3] - bbox[1])
    
    total_h = sum(line_h) + (len(lines) - 1) * 6
    curr_y = y1 + (h - total_h) / 2
    for i, line in enumerate(lines):
        lx = cx - line_w[i] / 2
        draw.text((lx, curr_y), line, font=font, fill=text_color)
        curr_y += line_h[i] + 6

def draw_ortho(draw, points, width=2, color='#000000', arrow_end=False):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=color, width=width)
    
    if arrow_end and len(points) >= 2:
        p_prev = points[-2]
        p_last = points[-1]
        x2, y2 = p_last
        x1, y1 = p_prev
        
        # Determine orientation
        if y2 > y1 and x2 == x1: # Moving down
            poly = [(x2, y2), (x2 - 7, y2 - 14), (x2 + 7, y2 - 14)]
            draw.polygon(poly, fill=color)
        elif y2 < y1 and x2 == x1: # Moving up
            poly = [(x2, y2), (x2 - 7, y2 + 14), (x2 + 7, y2 + 14)]
            draw.polygon(poly, fill=color)
        elif x2 > x1 and y2 == y1: # Moving right
            poly = [(x2, y2), (x2 - 14, y2 - 7), (x2 - 14, y2 + 7)]
            draw.polygon(poly, fill=color)
        elif x2 < x1 and y2 == y1: # Moving left
            poly = [(x2, y2), (x2 + 14, y2 - 7), (x2 + 14, y2 + 7)]
            draw.polygon(poly, fill=color)

def build_structure_chart_landscape(with_arrows=False):
    W = 2800
    H = 1250
    img = Image.new('RGB', (W, H), '#ffffff')
    draw = ImageDraw.Draw(img)
    
    # Fonts
    f_root = get_font(32, bold=True)
    f_l1 = get_font(24, bold=True)
    f_l2 = get_font(22, bold=True)
    f_leaf = get_font(20, bold=False)
    
    # Box dimensions
    root_w, root_h = 240, 70
    l1_h = 68
    l2_h = 60
    leaf_h = 52
    
    # Y Coordinates
    y_root = 85
    y_bus_main = 185
    y_l1 = 265
    
    # 5 Branch Centers along X
    x_b1 = 280   # Reports
    x_b2 = 660   # Attendance Management
    x_b3 = 1080  # App Users
    x_b4 = 1750  # Masters (spanning 1500 to 2140)
    x_b5 = 2480  # Maintenance Management
    
    # --- Root Node: Admin ---
    cx_root = 1380
    draw_box(draw, cx_root, y_root, root_w, root_h, "Admin", f_root, border_width=2)
    
    # Root drop to main bus
    draw_ortho(draw, [(cx_root, y_root + root_h / 2), (cx_root, y_bus_main)], width=2)
    # Main horizontal bus spanning from x_b1 to x_b5
    draw_ortho(draw, [(x_b1, y_bus_main), (x_b5, y_bus_main)], width=2)
    
    # Drop lines from main bus to L1 boxes
    for bx in [x_b1, x_b2, x_b3, x_b4, x_b5]:
        draw_ortho(draw, [(bx, y_bus_main), (bx, y_l1 - l1_h / 2)], width=2, arrow_end=with_arrows)
        
    # --- L1 Boxes ---
    draw_box(draw, x_b1, y_l1, 210, l1_h, "Reports", f_l1, border_width=2)
    draw_box(draw, x_b2, y_l1, 240, l1_h, "Attendance\nManagement", f_l1, border_width=2)
    draw_box(draw, x_b3, y_l1, 210, l1_h, "App Users", f_l1, border_width=2)
    draw_box(draw, x_b4, y_l1, 210, l1_h, "Masters", f_l1, border_width=2)
    draw_box(draw, x_b5, y_l1, 240, l1_h, "Maintenance\nManagement", f_l1, border_width=2)
    
    # ==========================================
    # BRANCH 1: Reports
    # ==========================================
    y_b1_sub = 370
    y_rep_l2 = 445
    y_rep_leaf = 575
    
    x_rep_daily = x_b1 - 100  # 180
    x_rep_month = x_b1 + 100  # 380
    
    # Bus under Reports
    draw_ortho(draw, [(x_b1, y_l1 + l1_h / 2), (x_b1, y_b1_sub)], width=2)
    draw_ortho(draw, [(x_rep_daily, y_b1_sub), (x_rep_month, y_b1_sub)], width=2)
    draw_ortho(draw, [(x_rep_daily, y_b1_sub), (x_rep_daily, y_rep_l2 - l2_h / 2)], width=2, arrow_end=with_arrows)
    draw_ortho(draw, [(x_rep_month, y_b1_sub), (x_rep_month, y_rep_l2 - l2_h / 2)], width=2, arrow_end=with_arrows)
    
    draw_box(draw, x_rep_daily, y_rep_l2, 170, l2_h, "Daily Logs", f_l2, border_width=2)
    draw_box(draw, x_rep_month, y_rep_l2, 170, l2_h, "Monthly", f_l2, border_width=2)
    
    # Drops straight down to Defaulters and Occupancy
    draw_ortho(draw, [(x_rep_daily, y_rep_l2 + l2_h / 2), (x_rep_daily, y_rep_leaf - leaf_h / 2)], width=2, arrow_end=with_arrows)
    draw_ortho(draw, [(x_rep_month, y_rep_l2 + l2_h / 2), (x_rep_month, y_rep_leaf - leaf_h / 2)], width=2, arrow_end=with_arrows)
    
    draw_box(draw, x_rep_daily, y_rep_leaf, 170, leaf_h, "Defaulters", f_leaf, border_width=2)
    draw_box(draw, x_rep_month, y_rep_leaf, 170, leaf_h, "Occupancy", f_leaf, border_width=2)
    
    # ==========================================
    # BRANCH 2: Attendance Management
    # ==========================================
    y_b2_bus = 490
    y_att_leaf = 575
    
    x_att_1 = x_b2 - 100  # 560
    x_att_2 = x_b2 + 100  # 760
    
    draw_ortho(draw, [(x_b2, y_l1 + l1_h / 2), (x_b2, y_b2_bus)], width=2)
    draw_ortho(draw, [(x_att_1, y_b2_bus), (x_att_2, y_b2_bus)], width=2)
    draw_ortho(draw, [(x_att_1, y_b2_bus), (x_att_1, y_att_leaf - leaf_h / 2)], width=2, arrow_end=with_arrows)
    draw_ortho(draw, [(x_att_2, y_b2_bus), (x_att_2, y_att_leaf - leaf_h / 2)], width=2, arrow_end=with_arrows)
    
    draw_box(draw, x_att_1, y_att_leaf, 175, leaf_h, "Mess Attendance", f_leaf, border_width=2)
    draw_box(draw, x_att_2, y_att_leaf, 175, leaf_h, "Staff Attendance", f_leaf, border_width=2)
    
    # ==========================================
    # BRANCH 3: App Users
    # ==========================================
    y_b3_bus = 490
    y_usr_leaf = 575
    
    x_u1 = x_b3 - 140  # 940
    x_u2 = x_b3        # 1080
    x_u3 = x_b3 + 140  # 1220
    
    draw_ortho(draw, [(x_b3, y_l1 + l1_h / 2), (x_b3, y_b3_bus)], width=2)
    draw_ortho(draw, [(x_u1, y_b3_bus), (x_u3, y_b3_bus)], width=2)
    for ux in [x_u1, x_u2, x_u3]:
        draw_ortho(draw, [(ux, y_b3_bus), (ux, y_usr_leaf - leaf_h / 2)], width=2, arrow_end=with_arrows)
        
    draw_box(draw, x_u1, y_usr_leaf, 125, leaf_h, "Tenants", f_leaf, border_width=2)
    draw_box(draw, x_u2, y_usr_leaf, 125, leaf_h, "Staff", f_leaf, border_width=2)
    draw_box(draw, x_u3, y_usr_leaf, 125, leaf_h, "Admin", f_leaf, border_width=2)
    
    # ==========================================
    # BRANCH 4: Masters (Rooms, Tenants, Employees with Staggered Add/Edit/Delete)
    # ==========================================
    x_m_rooms = 1500
    x_m_tenants = 1820
    x_m_staff = 2140
    
    y_m_bus = 370
    y_m_l2 = 445
    
    # Bus under Masters connecting Rooms, Tenants, Employees
    draw_ortho(draw, [(x_b4, y_l1 + l1_h / 2), (x_b4, y_m_bus)], width=2)
    draw_ortho(draw, [(x_m_rooms, y_m_bus), (x_m_staff, y_m_bus)], width=2)
    for mx in [x_m_rooms, x_m_tenants, x_m_staff]:
        draw_ortho(draw, [(mx, y_m_bus), (mx, y_m_l2 - l2_h / 2)], width=2, arrow_end=with_arrows)
        
    draw_box(draw, x_m_rooms, y_m_l2, 180, l2_h, "Rooms", f_l2, border_width=2)
    draw_box(draw, x_m_tenants, y_m_l2, 180, l2_h, "Tenants", f_l2, border_width=2)
    draw_box(draw, x_m_staff, y_m_l2, 180, l2_h, "Employees", f_l2, border_width=2)
    
    # Staggered Add, Edit, Delete for each
    crud_w = 95
    crud_gap = 105
    
    # 1. Rooms -> Step 1 (y = 575)
    y_r1_bus = 515
    y_r1_leaf = 575
    draw_ortho(draw, [(x_m_rooms, y_m_l2 + l2_h / 2), (x_m_rooms, y_r1_bus)], width=2)
    draw_ortho(draw, [(x_m_rooms - crud_gap, y_r1_bus), (x_m_rooms + crud_gap, y_r1_bus)], width=2)
    for cx, txt in zip([x_m_rooms - crud_gap, x_m_rooms, x_m_rooms + crud_gap], ["Add", "Edit", "Delete"]):
        draw_ortho(draw, [(cx, y_r1_bus), (cx, y_r1_leaf - leaf_h / 2)], width=2, arrow_end=with_arrows)
        draw_box(draw, cx, y_r1_leaf, crud_w, leaf_h, txt, f_leaf, border_width=2)
        
    # 2. Tenants -> Step 2 (staggered lower: y = 745)
    y_r2_bus = 685
    y_r2_leaf = 745
    draw_ortho(draw, [(x_m_tenants, y_m_l2 + l2_h / 2), (x_m_tenants, y_r2_bus)], width=2)
    draw_ortho(draw, [(x_m_tenants - crud_gap, y_r2_bus), (x_m_tenants + crud_gap, y_r2_bus)], width=2)
    for cx, txt in zip([x_m_tenants - crud_gap, x_m_tenants, x_m_tenants + crud_gap], ["Add", "Edit", "Delete"]):
        draw_ortho(draw, [(cx, y_r2_bus), (cx, y_r2_leaf - leaf_h / 2)], width=2, arrow_end=with_arrows)
        draw_box(draw, cx, y_r2_leaf, crud_w, leaf_h, txt, f_leaf, border_width=2)
        
    # 3. Employees -> Step 3 (staggered even lower: y = 915)
    y_r3_bus = 855
    y_r3_leaf = 915
    draw_ortho(draw, [(x_m_staff, y_m_l2 + l2_h / 2), (x_m_staff, y_r3_bus)], width=2)
    draw_ortho(draw, [(x_m_staff - crud_gap, y_r3_bus), (x_m_staff + crud_gap, y_r3_bus)], width=2)
    for cx, txt in zip([x_m_staff - crud_gap, x_m_staff, x_m_staff + crud_gap], ["Add", "Edit", "Delete"]):
        draw_ortho(draw, [(cx, y_r3_bus), (cx, y_r3_leaf - leaf_h / 2)], width=2, arrow_end=with_arrows)
        draw_box(draw, cx, y_r3_leaf, crud_w, leaf_h, txt, f_leaf, border_width=2)
        
    # ==========================================
    # BRANCH 5: Maintenance Management
    # ==========================================
    y_b5_bus = 515
    y_b5_leaf = 575
    draw_ortho(draw, [(x_b5, y_l1 + l1_h / 2), (x_b5, y_b5_bus)], width=2)
    draw_ortho(draw, [(x_b5 - crud_gap, y_b5_bus), (x_b5 + crud_gap, y_b5_bus)], width=2)
    for cx, txt in zip([x_b5 - crud_gap, x_b5, x_b5 + crud_gap], ["Add", "Edit", "Delete"]):
        draw_ortho(draw, [(cx, y_b5_bus), (cx, y_b5_leaf - leaf_h / 2)], width=2, arrow_end=with_arrows)
        draw_box(draw, cx, y_b5_leaf, crud_w, leaf_h, txt, f_leaf, border_width=2)
        
    # Crop tightly to content + padding
    crop_bottom = y_r3_leaf + leaf_h / 2 + 70
    return img.crop((0, 0, W, int(crop_bottom)))

def build_portrait_page(with_arrows=False):
    PW = 2480
    PH = 3508
    page = Image.new('RGB', (PW, PH), '#ffffff')
    draw = ImageDraw.Draw(page)
    
    f_header = get_font(44, bold=False, serif=False)
    f_caption = get_font(42, bold=False, serif=False)
    
    margin_x = 160
    header_y = 150
    draw.text((margin_x, header_y), "Roomzyy — Paying Guest Management System", font=f_header, fill='#222222')
    
    # Header double lines
    line1_y = header_y + 64
    line2_y = line1_y + 12
    draw.line([(margin_x, line1_y), (PW - margin_x, line1_y)], fill='#222222', width=5)
    draw.line([(margin_x, line2_y), (PW - margin_x, line2_y)], fill='#555555', width=2)
    
    # Corner registration crop marks
    crop_len = 55
    draw.line([(margin_x - 45, header_y - 25), (margin_x - 45 + crop_len, header_y - 25)], fill='#888888', width=2)
    draw.line([(margin_x - 45, header_y - 25), (margin_x - 45, header_y - 25 + crop_len)], fill='#888888', width=2)
    draw.line([(PW - margin_x + 45 - crop_len, header_y - 25), (PW - margin_x + 45, header_y - 25)], fill='#888888', width=2)
    draw.line([(PW - margin_x + 45, header_y - 25), (PW - margin_x + 45, header_y - 25 + crop_len)], fill='#888888', width=2)
    
    # Bottom Caption
    caption_text = "Fig 4.2.1.2 Structure Chart"
    bbox_cap = f_caption.getbbox(caption_text)
    cap_w = bbox_cap[2] - bbox_cap[0]
    draw.text(((PW - cap_w) / 2, PH - 230), caption_text, font=f_caption, fill='#111111')
    
    # Generate the landscape chart
    chart_img = build_structure_chart_landscape(with_arrows=with_arrows)
    
    # Rotate 270 (so top of chart is on the RIGHT, exactly matching user reference photo!)
    chart_rotated = chart_img.transpose(Image.ROTATE_270)
    
    # Fit into the available space
    avail_w = PW - 2 * margin_x
    avail_h = PH - line2_y - 340
    
    scale = min(avail_w / chart_rotated.width, avail_h / chart_rotated.height)
    new_w = int(chart_rotated.width * scale * 0.98)
    new_h = int(chart_rotated.height * scale * 0.98)
    
    chart_resized = chart_rotated.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    paste_x = int((PW - new_w) / 2)
    paste_y = int(line2_y + 40 + (avail_h - new_h) / 2)
    page.paste(chart_resized, (paste_x, paste_y))
    
    return page, chart_img

def main():
    docs_dir = r"c:\Users\divya\-Roomzyy\docs"
    brain_dir = r"C:\Users\divya\.gemini\antigravity-ide\brain\d9db20a6-b403-4b54-8645-97d76811b78e"
    os.makedirs(docs_dir, exist_ok=True)
    os.makedirs(brain_dir, exist_ok=True)
    
    # 1. Exact Reference Match (Without Arrow Marks - Solid Orthogonal Lines)
    print("Generating Structure Chart without arrows (Exact Reference Photo style)...")
    page_no_arrows, landscape_no_arrows = build_portrait_page(with_arrows=False)
    page_no_arrows.save(os.path.join(docs_dir, "Roomzyy_Structure_Chart_Page.png"), "PNG", dpi=(300, 300))
    page_no_arrows.save(os.path.join(brain_dir, "Roomzyy_Structure_Chart_Page.png"), "PNG", dpi=(300, 300))
    landscape_no_arrows.save(os.path.join(docs_dir, "Roomzyy_Structure_Chart_Landscape.png"), "PNG", dpi=(300, 300))
    landscape_no_arrows.save(os.path.join(brain_dir, "Roomzyy_Structure_Chart_Landscape.png"), "PNG", dpi=(300, 300))
    
    # 2. With Directional Arrowheads (Arrow marks style)
    print("Generating Structure Chart WITH arrows...")
    page_arrows, landscape_arrows = build_portrait_page(with_arrows=True)
    page_arrows.save(os.path.join(docs_dir, "Roomzyy_Structure_Chart_Page_Arrows.png"), "PNG", dpi=(300, 300))
    page_arrows.save(os.path.join(brain_dir, "Roomzyy_Structure_Chart_Page_Arrows.png"), "PNG", dpi=(300, 300))
    landscape_arrows.save(os.path.join(docs_dir, "Roomzyy_Structure_Chart_Landscape_Arrows.png"), "PNG", dpi=(300, 300))
    landscape_arrows.save(os.path.join(brain_dir, "Roomzyy_Structure_Chart_Landscape_Arrows.png"), "PNG", dpi=(300, 300))
    
    print("All versions generated successfully!")

if __name__ == '__main__':
    main()
