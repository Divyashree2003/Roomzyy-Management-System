import os
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    path = 'C:\\Windows\\Fonts\\arialbd.ttf' if bold else 'C:\\Windows\\Fonts\\arial.ttf'
    if os.path.exists(path):
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()

def draw_box(draw, cx, cy, w, h, text, font, border_width=3, bg_fill='#ffffff', border_color='#000000', text_color='#000000'):
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

def draw_ortho(draw, points, width=3, color='#000000', arrow_end=False):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=color, width=width)
    if arrow_end and len(points) >= 2:
        x1, y1 = points[-2]
        x2, y2 = points[-1]
        if y2 > y1 and x2 == x1: # Down
            poly = [(x2, y2), (x2 - 8, y2 - 16), (x2 + 8, y2 - 16)]
            draw.polygon(poly, fill=color)

def generate_zoomed_chart(with_arrows=True):
    # Compact high-density canvas
    W = 2500
    H = 1150
    img = Image.new('RGB', (W, H), '#ffffff')
    draw = ImageDraw.Draw(img)
    
    # Large, bold, readable fonts
    f_root = get_font(36, bold=True)
    f_l1 = get_font(26, bold=True)
    f_l2 = get_font(24, bold=True)
    f_leaf = get_font(22, bold=True)
    
    # Box dimensions
    root_w, root_h = 240, 75
    l1_h = 75
    l2_h = 65
    leaf_h = 58
    
    # Y Coordinates
    y_root = 70
    y_bus_main = 160
    y_l1 = 235
    
    # 5 Branches along X
    x_b1 = 250   # Reports
    x_b2 = 590   # Attendance Management
    x_b3 = 960   # App Users
    x_b4 = 1570  # Masters (spanning 1340, 1630, 1920)
    x_b5 = 2240  # Maintenance Management
    
    # Root: Admin
    cx_root = 1240
    draw_box(draw, cx_root, y_root, root_w, root_h, "Admin", f_root, border_width=4)
    
    # Drop from Admin to main bus
    draw_ortho(draw, [(cx_root, y_root + root_h / 2), (cx_root, y_bus_main)], width=3)
    draw_ortho(draw, [(x_b1, y_bus_main), (x_b5, y_bus_main)], width=3)
    
    # Drop to L1
    for bx in [x_b1, x_b2, x_b3, x_b4, x_b5]:
        draw_ortho(draw, [(bx, y_bus_main), (bx, y_l1 - l1_h / 2)], width=3, arrow_end=with_arrows)
        
    draw_box(draw, x_b1, y_l1, 200, l1_h, "Reports", f_l1, border_width=3)
    draw_box(draw, x_b2, y_l1, 220, l1_h, "Attendance\nManagement", f_l1, border_width=3)
    draw_box(draw, x_b3, y_l1, 200, l1_h, "App Users", f_l1, border_width=3)
    draw_box(draw, x_b4, y_l1, 200, l1_h, "Masters", f_l1, border_width=3)
    draw_box(draw, x_b5, y_l1, 220, l1_h, "Maintenance\nManagement", f_l1, border_width=3)
    
    # --- Branch 1: Reports ---
    y_b1_sub = 330
    y_rep_l2 = 405
    y_rep_leaf = 525
    x_daily = x_b1 - 95  # 155
    x_month = x_b1 + 95  # 345
    
    draw_ortho(draw, [(x_b1, y_l1 + l1_h / 2), (x_b1, y_b1_sub)], width=3)
    draw_ortho(draw, [(x_daily, y_b1_sub), (x_month, y_b1_sub)], width=3)
    draw_ortho(draw, [(x_daily, y_b1_sub), (x_daily, y_rep_l2 - l2_h / 2)], width=3, arrow_end=with_arrows)
    draw_ortho(draw, [(x_month, y_b1_sub), (x_month, y_rep_l2 - l2_h / 2)], width=3, arrow_end=with_arrows)
    draw_box(draw, x_daily, y_rep_l2, 160, l2_h, "Daily Logs", f_l2, border_width=3)
    draw_box(draw, x_month, y_rep_l2, 160, l2_h, "Monthly", f_l2, border_width=3)
    
    draw_ortho(draw, [(x_daily, y_rep_l2 + l2_h / 2), (x_daily, y_rep_leaf - leaf_h / 2)], width=3, arrow_end=with_arrows)
    draw_ortho(draw, [(x_month, y_rep_l2 + l2_h / 2), (x_month, y_rep_leaf - leaf_h / 2)], width=3, arrow_end=with_arrows)
    draw_box(draw, x_daily, y_rep_leaf, 160, leaf_h, "Defaulters", f_leaf, border_width=3)
    draw_box(draw, x_month, y_rep_leaf, 160, leaf_h, "Occupancy", f_leaf, border_width=3)
    
    # --- Branch 2: Attendance Management ---
    y_b2_bus = 445
    y_att_leaf = 525
    x_att1 = x_b2 - 95
    x_att2 = x_b2 + 95
    draw_ortho(draw, [(x_b2, y_l1 + l1_h / 2), (x_b2, y_b2_bus)], width=3)
    draw_ortho(draw, [(x_att1, y_b2_bus), (x_att2, y_b2_bus)], width=3)
    draw_ortho(draw, [(x_att1, y_b2_bus), (x_att1, y_att_leaf - leaf_h / 2)], width=3, arrow_end=with_arrows)
    draw_ortho(draw, [(x_att2, y_b2_bus), (x_att2, y_att_leaf - leaf_h / 2)], width=3, arrow_end=with_arrows)
    draw_box(draw, x_att1, y_att_leaf, 175, leaf_h, "Mess Attendance", f_leaf, border_width=3)
    draw_box(draw, x_att2, y_att_leaf, 175, leaf_h, "Staff Attendance", f_leaf, border_width=3)
    
    # --- Branch 3: App Users ---
    y_b3_bus = 445
    y_usr_leaf = 525
    x_u1 = x_b3 - 125
    x_u2 = x_b3
    x_u3 = x_b3 + 125
    draw_ortho(draw, [(x_b3, y_l1 + l1_h / 2), (x_b3, y_b3_bus)], width=3)
    draw_ortho(draw, [(x_u1, y_b3_bus), (x_u3, y_b3_bus)], width=3)
    for ux in [x_u1, x_u2, x_u3]:
        draw_ortho(draw, [(ux, y_b3_bus), (ux, y_usr_leaf - leaf_h / 2)], width=3, arrow_end=with_arrows)
    draw_box(draw, x_u1, y_usr_leaf, 115, leaf_h, "Tenants", f_leaf, border_width=3)
    draw_box(draw, x_u2, y_usr_leaf, 115, leaf_h, "Staff", f_leaf, border_width=3)
    draw_box(draw, x_u3, y_usr_leaf, 115, leaf_h, "Admin", f_leaf, border_width=3)
    
    # --- Branch 4: Masters ---
    x_m_rooms = 1350
    x_m_tenants = 1630
    x_m_staff = 1910
    y_m_bus = 330
    y_m_l2 = 405
    
    draw_ortho(draw, [(x_b4, y_l1 + l1_h / 2), (x_b4, y_m_bus)], width=3)
    draw_ortho(draw, [(x_m_rooms, y_m_bus), (x_m_staff, y_m_bus)], width=3)
    for mx in [x_m_rooms, x_m_tenants, x_m_staff]:
        draw_ortho(draw, [(mx, y_m_bus), (mx, y_m_l2 - l2_h / 2)], width=3, arrow_end=with_arrows)
    draw_box(draw, x_m_rooms, y_m_l2, 160, l2_h, "Rooms", f_l2, border_width=3)
    draw_box(draw, x_m_tenants, y_m_l2, 160, l2_h, "Tenants", f_l2, border_width=3)
    draw_box(draw, x_m_staff, y_m_l2, 160, l2_h, "Employees", f_l2, border_width=3)
    
    crud_w = 90
    crud_gap = 96
    
    # Rooms (y = 525)
    y_r1_bus = 465
    y_r1_leaf = 525
    draw_ortho(draw, [(x_m_rooms, y_m_l2 + l2_h / 2), (x_m_rooms, y_r1_bus)], width=3)
    draw_ortho(draw, [(x_m_rooms - crud_gap, y_r1_bus), (x_m_rooms + crud_gap, y_r1_bus)], width=3)
    for cx, txt in zip([x_m_rooms - crud_gap, x_m_rooms, x_m_rooms + crud_gap], ["Add", "Edit", "Delete"]):
        draw_ortho(draw, [(cx, y_r1_bus), (cx, y_r1_leaf - leaf_h / 2)], width=3, arrow_end=with_arrows)
        draw_box(draw, cx, y_r1_leaf, crud_w, leaf_h, txt, f_leaf, border_width=3)
        
    # Tenants (y = 675)
    y_r2_bus = 615
    y_r2_leaf = 675
    draw_ortho(draw, [(x_m_tenants, y_m_l2 + l2_h / 2), (x_m_tenants, y_r2_bus)], width=3)
    draw_ortho(draw, [(x_m_tenants - crud_gap, y_r2_bus), (x_m_tenants + crud_gap, y_r2_bus)], width=3)
    for cx, txt in zip([x_m_tenants - crud_gap, x_m_tenants, x_m_tenants + crud_gap], ["Add", "Edit", "Delete"]):
        draw_ortho(draw, [(cx, y_r2_bus), (cx, y_r2_leaf - leaf_h / 2)], width=3, arrow_end=with_arrows)
        draw_box(draw, cx, y_r2_leaf, crud_w, leaf_h, txt, f_leaf, border_width=3)
        
    # Employees (y = 825)
    y_r3_bus = 765
    y_r3_leaf = 825
    draw_ortho(draw, [(x_m_staff, y_m_l2 + l2_h / 2), (x_m_staff, y_r3_bus)], width=3)
    draw_ortho(draw, [(x_m_staff - crud_gap, y_r3_bus), (x_m_staff + crud_gap, y_r3_bus)], width=3)
    for cx, txt in zip([x_m_staff - crud_gap, x_m_staff, x_m_staff + crud_gap], ["Add", "Edit", "Delete"]):
        draw_ortho(draw, [(cx, y_r3_bus), (cx, y_r3_leaf - leaf_h / 2)], width=3, arrow_end=with_arrows)
        draw_box(draw, cx, y_r3_leaf, crud_w, leaf_h, txt, f_leaf, border_width=3)
        
    # --- Branch 5: Maintenance Management ---
    y_b5_bus = 465
    y_b5_leaf = 525
    draw_ortho(draw, [(x_b5, y_l1 + l1_h / 2), (x_b5, y_b5_bus)], width=3)
    draw_ortho(draw, [(x_b5 - crud_gap, y_b5_bus), (x_b5 + crud_gap, y_b5_bus)], width=3)
    for cx, txt in zip([x_b5 - crud_gap, x_b5, x_b5 + crud_gap], ["Add", "Edit", "Delete"]):
        draw_ortho(draw, [(cx, y_b5_bus), (cx, y_b5_leaf - leaf_h / 2)], width=3, arrow_end=with_arrows)
        draw_box(draw, cx, y_b5_leaf, crud_w, leaf_h, txt, f_leaf, border_width=3)
        
    # Crop tightly to non-white pixels + 40px margin
    from PIL import ImageOps
    gray = img.convert('L')
    inv = ImageOps.invert(gray)
    bbox = inv.getbbox()
    pad = 40
    crop_area = (max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(W, bbox[2] + pad), min(H, bbox[3] + pad))
    cropped = img.crop(crop_area)
    return cropped

if __name__ == '__main__':
    docs_dir = r"c:\Users\divya\-Roomzyy\docs"
    brain_dir = r"C:\Users\divya\.gemini\antigravity-ide\brain\d9db20a6-b403-4b54-8645-97d76811b78e"
    
    # 1. Zoomed Landscape (Upright, Large, High-Contrast)
    img_zoom_arrows = generate_zoomed_chart(with_arrows=True)
    img_zoom_arrows.save(os.path.join(docs_dir, "Roomzyy_Structure_Chart_Zoom_Landscape.png"))
    img_zoom_arrows.save(os.path.join(brain_dir, "Roomzyy_Structure_Chart_Zoom_Landscape.png"))
    
    # 2. Zoomed Rotated (Matching Reference Scan Orientation, but cropped tightly around chart!)
    img_zoom_vert = img_zoom_arrows.transpose(Image.ROTATE_270)
    img_zoom_vert.save(os.path.join(docs_dir, "Roomzyy_Structure_Chart_Zoom_Vertical.png"))
    img_zoom_vert.save(os.path.join(brain_dir, "Roomzyy_Structure_Chart_Zoom_Vertical.png"))
    
    # 3. Zoomed Plain Lines (No Arrows)
    img_zoom_plain = generate_zoomed_chart(with_arrows=False)
    img_zoom_plain.save(os.path.join(docs_dir, "Roomzyy_Structure_Chart_Zoom_Plain.png"))
    img_zoom_plain.save(os.path.join(brain_dir, "Roomzyy_Structure_Chart_Zoom_Plain.png"))
    
    # 4. Crop individual clean sections for ultra-detailed closeups:
    # Section A: Left modules (Admin, Reports, Attendance, App Users)
    sec_a = img_zoom_arrows.crop((0, 0, 1180, img_zoom_arrows.height))
    sec_a.save(os.path.join(docs_dir, "Zoom_Section_Reports_Users.png"))
    sec_a.save(os.path.join(brain_dir, "Zoom_Section_Reports_Users.png"))
    
    # Section B: Right modules (Masters with staggered CRUD & Maintenance)
    sec_b = img_zoom_arrows.crop((1160, 0, img_zoom_arrows.width, img_zoom_arrows.height))
    sec_b.save(os.path.join(docs_dir, "Zoom_Section_Masters_Maintenance.png"))
    sec_b.save(os.path.join(brain_dir, "Zoom_Section_Masters_Maintenance.png"))
    
    print("All Zoom images generated successfully!")
