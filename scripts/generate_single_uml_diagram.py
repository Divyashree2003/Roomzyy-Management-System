import os
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False, italic=False, serif=True):
    if serif:
        if bold and italic:
            path = 'C:\\Windows\\Fonts\\timesbi.ttf'
        elif bold:
            path = 'C:\\Windows\\Fonts\\timesbd.ttf'
        elif italic:
            path = 'C:\\Windows\\Fonts\\timesi.ttf'
        else:
            path = 'C:\\Windows\\Fonts\\times.ttf'
    else:
        if bold and italic:
            path = 'C:\\Windows\\Fonts\\arialbi.ttf'
        elif bold:
            path = 'C:\\Windows\\Fonts\\arialbd.ttf'
        elif italic:
            path = 'C:\\Windows\\Fonts\\ariali.ttf'
        else:
            path = 'C:\\Windows\\Fonts\\arial.ttf'
    
    if os.path.exists(path):
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()

def draw_uml_class(draw, x1, y1, width, title, attributes, methods, f_title, f_body, pad_y=10, pad_x=16):
    bbox_t = f_title.getbbox(title)
    h_title = (bbox_t[3] - bbox_t[1]) + pad_y * 2
    
    line_h_attr = []
    for attr in attributes:
        bb = f_body.getbbox(attr)
        line_h_attr.append(bb[3] - bb[1] + 6)
    h_attr = sum(line_h_attr) + pad_y * 1.2 if attributes else 0
    
    line_h_meth = []
    for meth in methods:
        bb = f_body.getbbox(meth)
        line_h_meth.append(bb[3] - bb[1] + 6)
    h_meth = sum(line_h_meth) + pad_y * 1.2 if methods else 0
    
    total_h = h_title + h_attr + h_meth
    x2 = x1 + width
    y2 = y1 + total_h
    
    # Box outline
    draw.rectangle([x1, y1, x2, y2], fill='#ffffff', outline='#000000', width=2)
    
    # Title divider & text
    draw.line([(x1, y1 + h_title), (x2, y1 + h_title)], fill='#000000', width=2)
    title_w = bbox_t[2] - bbox_t[0]
    draw.text((x1 + (width - title_w) / 2, y1 + pad_y - 2), title, font=f_title, fill='#000000')
    
    # Attributes
    curr_y = y1 + h_title + pad_y * 0.7
    for i, attr in enumerate(attributes):
        draw.text((x1 + pad_x, curr_y), attr, font=f_body, fill='#000000')
        curr_y += line_h_attr[i]
        
    # Methods divider & text
    if methods:
        draw.line([(x1, y1 + h_title + h_attr), (x2, y1 + h_title + h_attr)], fill='#000000', width=2)
        curr_y = y1 + h_title + h_attr + pad_y * 0.7
        for i, meth in enumerate(methods):
            draw.text((x1 + pad_x, curr_y), meth, font=f_body, fill='#000000')
            curr_y += line_h_meth[i]
            
    return (x1, y1, x2, y2)

def build_single_uml_diagram_image():
    # Dimensions for unified system UML diagram
    W = 2600
    H = 2050
    img = Image.new('RGB', (W, H), '#ffffff')
    draw = ImageDraw.Draw(img)
    
    f_title = get_font(28, bold=True, serif=True)
    f_body = get_font(22, bold=False, serif=True)
    f_mult = get_font(22, bold=False, serif=True)
    f_label = get_font(21, italic=True, serif=True)
    
    box_w = 460
    
    # ------------------ CLASS DEFINITIONS ------------------
    
    # 1. User (Top Center-Left)
    user_attrs = [
        "id: int",
        "email: string",
        "password_hash: string",
        "name: string",
        "role: string",
        "phone: string",
        "is_active: boolean"
    ]
    user_meths = [
        "login()",
        "verifyOtp()",
        "resetPassword()"
    ]
    box_user = draw_uml_class(draw, 1070, 60, box_w, "User", user_attrs, user_meths, f_title, f_body)
    
    # 2. Employee (Top Right)
    emp_attrs = [
        "id: int",
        "user_id: int",
        "role: string",
        "salary: float",
        "default_shift: string",
        "active: boolean"
    ]
    emp_meths = [
        "markAttendance()",
        "assignDuty()",
        "updateDutyStatus()"
    ]
    box_emp = draw_uml_class(draw, 1950, 60, box_w + 40, "Employee", emp_attrs, emp_meths, f_title, f_body)
    
    # 3. Room (Middle Left)
    room_attrs = [
        "id: int",
        "room_number: string",
        "room_type: string",
        "floor: string",
        "capacity: int",
        "monthly_rent: float",
        "status: string"
    ]
    room_meths = [
        "addRoom()",
        "allocateBed()",
        "vacateBed()",
        "updateStatus()"
    ]
    box_room = draw_uml_class(draw, 100, 680, box_w, "Room", room_attrs, room_meths, f_title, f_body)
    
    # 4. Tenant (Middle Center)
    tenant_attrs = [
        "id: int",
        "user_id: int",
        "room_id: int",
        "id_proof_type: string",
        "id_proof_status: string",
        "emergency_contact: string",
        "status: string"
    ]
    tenant_meths = [
        "selectRoom()",
        "payDirectRent()",
        "optInMeal()",
        "requestVisitorPass()",
        "raiseMaintenance()"
    ]
    box_tenant = draw_uml_class(draw, 1070, 680, box_w, "Tenant", tenant_attrs, tenant_meths, f_title, f_body)
    
    # 5. RentPayment (Middle Right - Direct Payment, No Razorpay!)
    rent_attrs = [
        "id: int",
        "tenant_id: int",
        "month: string",
        "amount: float",
        "due_date: date",
        "payment_method: string",
        "status: string",
        "receipt_number: string"
    ]
    rent_meths = [
        "recordDirectPayment()",
        "generateReceiptPdf()",
        "sendReminder()"
    ]
    box_rent = draw_uml_class(draw, 1950, 680, box_w + 40, "RentPayment (Direct)", rent_attrs, rent_meths, f_title, f_body)
    
    # 6. MealAttendance (Bottom Left)
    meal_attrs = [
        "id: int",
        "tenant_id: int",
        "date: date",
        "meal_type: string",
        "opted_in: boolean",
        "present: boolean",
        "diet: string"
    ]
    meal_meths = [
        "optInMeal()",
        "markAttendance()",
        "submitFeedback()"
    ]
    box_meal = draw_uml_class(draw, 100, 1370, box_w, "MealAttendance", meal_attrs, meal_meths, f_title, f_body)
    
    # 7. VisitorPass (Bottom Center)
    vis_attrs = [
        "id: int",
        "tenant_id: int",
        "visitor_name: string",
        "phone: string",
        "visit_date: date",
        "pass_code: string",
        "approval_status: string"
    ]
    vis_meths = [
        "generatePass()",
        "verifyQrCode()",
        "markCheckIn()",
        "markCheckOut()"
    ]
    box_vis = draw_uml_class(draw, 1070, 1370, box_w, "VisitorPass", vis_attrs, vis_meths, f_title, f_body)
    
    # 8. MaintenanceRequest (Bottom Right)
    maint_attrs = [
        "id: int",
        "tenant_id: int",
        "room_id: int",
        "category: string",
        "description: string",
        "priority: string",
        "status: string",
        "assigned_to: int"
    ]
    maint_meths = [
        "logComplaint()",
        "assignStaff()",
        "resolveIssue()"
    ]
    box_maint = draw_uml_class(draw, 1950, 1370, box_w + 40, "MaintenanceRequest", maint_attrs, maint_meths, f_title, f_body)

    # ------------------ RELATIONSHIPS & MULTIPLICITY ------------------
    
    # 1. User to Tenant (Vertical: User bottom -> Tenant top)
    draw.line([(box_user[0] + box_w / 2, box_user[3]), (box_tenant[0] + box_w / 2, box_tenant[1])], fill='#000000', width=2)
    draw.text((box_user[0] + box_w / 2 + 10, box_user[3] + 15), "1", font=f_mult, fill='#000000')
    draw.text((box_tenant[0] + box_w / 2 + 10, box_tenant[1] - 35), "0..1", font=f_mult, fill='#000000')
    draw.text((box_user[0] + box_w / 2 + 14, (box_user[3] + box_tenant[1]) / 2 - 12), "Identifies", font=f_label, fill='#000000')
    
    # 2. User to Employee (Horizontal: User right -> Employee left)
    draw.line([(box_user[2], box_user[1] + 120), (box_emp[0], box_emp[1] + 120)], fill='#000000', width=2)
    draw.text((box_user[2] + 15, box_user[1] + 85), "1", font=f_mult, fill='#000000')
    draw.text((box_emp[0] - 45, box_emp[1] + 85), "0..1", font=f_mult, fill='#000000')
    draw.text(((box_user[2] + box_emp[0]) / 2 - 25, box_user[1] + 90), "Employs", font=f_label, fill='#000000')
    
    # 3. Room to Tenant (Horizontal: Room right -> Tenant left)
    draw.line([(box_room[2], box_room[1] + 150), (box_tenant[0], box_tenant[1] + 150)], fill='#000000', width=2)
    draw.text((box_room[2] + 15, box_room[1] + 115), "1", font=f_mult, fill='#000000')
    draw.text((box_tenant[0] - 30, box_tenant[1] + 115), "*", font=f_mult, fill='#000000')
    draw.text(((box_room[2] + box_tenant[0]) / 2 - 25, box_room[1] + 120), "Occupies", font=f_label, fill='#000000')
    
    # 4. Tenant to RentPayment (Horizontal: Tenant right -> RentPayment left)
    draw.line([(box_tenant[2], box_tenant[1] + 150), (box_rent[0], box_rent[1] + 150)], fill='#000000', width=2)
    draw.text((box_tenant[2] + 15, box_tenant[1] + 115), "1", font=f_mult, fill='#000000')
    draw.text((box_rent[0] - 30, box_rent[1] + 115), "*", font=f_mult, fill='#000000')
    draw.text(((box_tenant[2] + box_rent[0]) / 2 - 15, box_tenant[1] + 120), "Pays", font=f_label, fill='#000000')
    
    # 5. Tenant to VisitorPass (Vertical: Tenant bottom -> VisitorPass top)
    draw.line([(box_tenant[0] + box_w / 2, box_tenant[3]), (box_vis[0] + box_w / 2, box_vis[1])], fill='#000000', width=2)
    draw.text((box_tenant[0] + box_w / 2 + 10, box_tenant[3] + 15), "1", font=f_mult, fill='#000000')
    draw.text((box_vis[0] + box_w / 2 + 10, box_vis[1] - 35), "*", font=f_mult, fill='#000000')
    draw.text((box_tenant[0] + box_w / 2 + 14, (box_tenant[3] + box_vis[1]) / 2 - 12), "Requests", font=f_label, fill='#000000')
    
    # 6. Tenant to MealAttendance (Diagonal left: Tenant bottom-left -> MealAttendance top-right)
    draw.line([(box_tenant[0] + 60, box_tenant[3]), (box_meal[2] - 30, box_meal[1])], fill='#000000', width=2)
    draw.text((box_tenant[0] + 30, box_tenant[3] + 15), "1", font=f_mult, fill='#000000')
    draw.text((box_meal[2] - 15, box_meal[1] - 30), "*", font=f_mult, fill='#000000')
    draw.text(((box_tenant[0] + 60 + box_meal[2]) / 2 - 30, (box_tenant[3] + box_meal[1]) / 2 - 15), "Opts-in", font=f_label, fill='#000000')
    
    # 7. Tenant to MaintenanceRequest (Diagonal right: Tenant bottom-right -> Maintenance top-left)
    draw.line([(box_tenant[2] - 60, box_tenant[3]), (box_maint[0] + 40, box_maint[1])], fill='#000000', width=2)
    draw.text((box_tenant[2] - 45, box_tenant[3] + 15), "1", font=f_mult, fill='#000000')
    draw.text((box_maint[0] + 15, box_maint[1] - 30), "*", font=f_mult, fill='#000000')
    draw.text(((box_tenant[2] - 60 + box_maint[0]) / 2 + 15, (box_tenant[3] + box_maint[1]) / 2 - 15), "Raises", font=f_label, fill='#000000')
    
    # 8. Employee to MaintenanceRequest (Vertical: Employee bottom -> Maintenance top)
    draw.line([(box_emp[0] + (box_w + 40) / 2, box_emp[3]), (box_maint[0] + (box_w + 40) / 2, box_maint[1])], fill='#000000', width=2)
    draw.text((box_emp[0] + (box_w + 40) / 2 + 10, box_emp[3] + 15), "1", font=f_mult, fill='#000000')
    draw.text((box_maint[0] + (box_w + 40) / 2 + 10, box_maint[1] - 35), "*", font=f_mult, fill='#000000')
    draw.text((box_emp[0] + (box_w + 40) / 2 + 14, (box_emp[3] + box_maint[1]) / 2 - 12), "Resolves", font=f_label, fill='#000000')

    max_y = max(box_meal[3], box_vis[3], box_maint[3]) + 60
    return img.crop((0, 0, W, max_y))

def build_portrait_single_uml_page():
    PW = 2480
    PH = 3508
    page = Image.new('RGB', (PW, PH), '#ffffff')
    draw = ImageDraw.Draw(page)
    
    f_header = get_font(42, bold=True, serif=True)
    f_body_text = get_font(30, bold=False, serif=True)
    f_caption = get_font(36, bold=False, serif=True)
    f_footer = get_font(28, bold=True, serif=True)
    
    margin_x = 160
    header_y = 150
    draw.text((margin_x, header_y), "Roomzyy — Paying Guest Management System", font=f_header, fill='#222222')
    
    # Header double lines
    line1_y = header_y + 60
    line2_y = line1_y + 10
    draw.line([(margin_x, line1_y), (PW - margin_x, line1_y)], fill='#444444', width=4)
    draw.line([(margin_x, line2_y), (PW - margin_x, line2_y)], fill='#777777', width=2)
    
    # Intro text
    intro_lines = [
        "The unified UML class diagram below models the core domain entities of Roomzyy. It shows the structural",
        "relationships between users, tenants, room allocations, direct rent payments (cash, UPI, and bank transfer),",
        "visitor passes, meal opt-ins, staff duties, and maintenance complaints across the entire property."
    ]
    curr_y = line2_y + 35
    for line in intro_lines:
        draw.text((margin_x, curr_y), line, font=f_body_text, fill='#222222')
        curr_y += 44
        
    diag_img = build_single_uml_diagram_image()
    
    # Scale to fit nicely between intro and caption
    avail_w = PW - 2 * margin_x
    avail_h = PH - curr_y - 420
    scale = min(avail_w / diag_img.width, avail_h / diag_img.height) * 0.98
    new_w = int(diag_img.width * scale)
    new_h = int(diag_img.height * scale)
    
    diag_resized = diag_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    paste_x = int((PW - new_w) / 2)
    paste_y = int(curr_y + 30 + (avail_h - new_h) / 2)
    page.paste(diag_resized, (paste_x, paste_y))
    
    caption_text = "Fig 4.2.1.3 Unified UML Class Diagram"
    bbox_cap = f_caption.getbbox(caption_text)
    cap_w = bbox_cap[2] - bbox_cap[0]
    draw.text(((PW - cap_w) / 2, paste_y + new_h + 45), caption_text, font=f_caption, fill='#111111')
    
    # Double line footer separator
    line_f1 = PH - 220
    line_f2 = line_f1 + 8
    draw.line([(margin_x, line_f1), (PW - margin_x, line_f1)], fill='#555555', width=4)
    draw.line([(margin_x, line_f2), (PW - margin_x, line_f2)], fill='#777777', width=2)
    
    draw.text((margin_x, line_f2 + 20), "Department of MCA", font=f_footer, fill='#555555')
    
    page_txt = "Page | 45"
    bbox_p = f_footer.getbbox(page_txt)
    pw = bbox_p[2] - bbox_p[0]
    draw.text(((PW - pw) / 2, line_f2 + 20), page_txt, font=f_footer, fill='#555555')
    
    pim_txt = "PIM, Udupi"
    bbox_pim = f_footer.getbbox(pim_txt)
    pim_w = bbox_pim[2] - bbox_pim[0]
    draw.text((PW - margin_x - pim_w, line_f2 + 20), pim_txt, font=f_footer, fill='#555555')
    
    return page

def generate_single_uml_svg():
    W = 1400
    H = 1050
    
    svg = []
    svg.append(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; font-family:\'Times New Roman\', Times, serif;">')
    svg.append('<style>')
    svg.append('  .box { fill:#ffffff; stroke:#111111; stroke-width:1.6; }')
    svg.append('  .line { stroke:#111111; stroke-width:1.6; fill:none; }')
    svg.append('  .title { font-size:15px; font-weight:bold; text-anchor:middle; fill:#000; }')
    svg.append('  .body { font-size:11.5px; text-anchor:start; fill:#000; }')
    svg.append('  .assoc { font-size:12px; font-style:italic; fill:#000; }')
    svg.append('  .mult { font-size:12px; fill:#000; }')
    svg.append('</style>')
    
    bw = 250
    
    # 1. User
    ux, uy, uh = 575, 30, 185
    svg.append(f'<rect class="box" x="{ux}" y="{uy}" width="{bw}" height="{uh}"/>')
    svg.append(f'<line class="line" x1="{ux}" y1="{uy + 28}" x2="{ux + bw}" y2="{uy + 28}"/>')
    svg.append(f'<text class="title" x="{ux + bw/2}" y="{uy + 20}">User</text>')
    u_attrs = ["id: int", "email: string", "password_hash: string", "name: string", "role: string", "is_active: boolean"]
    ay = uy + 44
    for a in u_attrs:
        svg.append(f'<text class="body" x="{ux + 10}" y="{ay}">{a}</text>')
        ay += 15
    svg.append(f'<line class="line" x1="{ux}" y1="{ay + 4}" x2="{ux + bw}" y2="{ay + 4}"/>')
    my = ay + 20
    for m in ["login()", "resetPassword()"]:
        svg.append(f'<text class="body" x="{ux + 10}" y="{my}">{m}</text>')
        my += 15

    # 2. Employee
    ex, ey, eh = 1050, 30, 185
    svg.append(f'<rect class="box" x="{ex}" y="{ey}" width="{bw}" height="{eh}"/>')
    svg.append(f'<line class="line" x1="{ex}" y1="{ey + 28}" x2="{ex + bw}" y2="{ey + 28}"/>')
    svg.append(f'<text class="title" x="{ex + bw/2}" y="{ey + 20}">Employee</text>')
    e_attrs = ["id: int", "user_id: int", "role: string", "salary: float", "default_shift: string", "active: boolean"]
    ay = ey + 44
    for a in e_attrs:
        svg.append(f'<text class="body" x="{ex + 10}" y="{ay}">{a}</text>')
        ay += 15
    svg.append(f'<line class="line" x1="{ex}" y1="{ay + 4}" x2="{ex + bw}" y2="{ay + 4}"/>')
    my = ay + 20
    for m in ["markAttendance()", "assignDuty()"]:
        svg.append(f'<text class="body" x="{ex + 10}" y="{my}">{m}</text>')
        my += 15

    # 3. Room
    rx, ry, rh = 100, 360, 200
    svg.append(f'<rect class="box" x="{rx}" y="{ry}" width="{bw}" height="{rh}"/>')
    svg.append(f'<line class="line" x1="{rx}" y1="{ry + 28}" x2="{rx + bw}" y2="{ry + 28}"/>')
    svg.append(f'<text class="title" x="{rx + bw/2}" y="{ry + 20}">Room</text>')
    r_attrs = ["id: int", "room_number: string", "room_type: string", "floor: string", "capacity: int", "monthly_rent: float", "status: string"]
    ay = ry + 44
    for a in r_attrs:
        svg.append(f'<text class="body" x="{rx + 10}" y="{ay}">{a}</text>')
        ay += 15
    svg.append(f'<line class="line" x1="{rx}" y1="{ay + 4}" x2="{rx + bw}" y2="{ay + 4}"/>')
    my = ay + 20
    for m in ["addRoom()", "allocateBed()", "vacateBed()"]:
        svg.append(f'<text class="body" x="{rx + 10}" y="{my}">{m}</text>')
        my += 15

    # 4. Tenant
    tx, ty, th = 575, 360, 220
    svg.append(f'<rect class="box" x="{tx}" y="{ty}" width="{bw}" height="{th}"/>')
    svg.append(f'<line class="line" x1="{tx}" y1="{ty + 28}" x2="{tx + bw}" y2="{ty + 28}"/>')
    svg.append(f'<text class="title" x="{tx + bw/2}" y="{ty + 20}">Tenant</text>')
    t_attrs = ["id: int", "user_id: int", "room_id: int", "id_proof_status: string", "emergency_contact: string", "status: string"]
    ay = ty + 44
    for a in t_attrs:
        svg.append(f'<text class="body" x="{tx + 10}" y="{ay}">{a}</text>')
        ay += 15
    svg.append(f'<line class="line" x1="{tx}" y1="{ay + 4}" x2="{tx + bw}" y2="{ay + 4}"/>')
    my = ay + 20
    for m in ["selectRoom()", "payDirectRent()", "optInMeal()", "requestVisitorPass()"]:
        svg.append(f'<text class="body" x="{tx + 10}" y="{my}">{m}</text>')
        my += 15

    # 5. RentPayment (Direct)
    px, py, ph = 1050, 360, 215
    svg.append(f'<rect class="box" x="{px}" y="{py}" width="{bw}" height="{ph}"/>')
    svg.append(f'<line class="line" x1="{px}" y1="{py + 28}" x2="{px + bw}" y2="{py + 28}"/>')
    svg.append(f'<text class="title" x="{px + bw/2}" y="{py + 20}">RentPayment (Direct)</text>')
    p_attrs = ["id: int", "tenant_id: int", "month: string", "amount: float", "due_date: date", "payment_method: string", "status: string", "receipt_number: string"]
    ay = py + 44
    for a in p_attrs:
        svg.append(f'<text class="body" x="{px + 10}" y="{ay}">{a}</text>')
        ay += 15
    svg.append(f'<line class="line" x1="{px}" y1="{ay + 4}" x2="{px + bw}" y2="{ay + 4}"/>')
    my = ay + 20
    for m in ["recordDirectPayment()", "generateReceiptPdf()"]:
        svg.append(f'<text class="body" x="{px + 10}" y="{my}">{m}</text>')
        my += 15

    # 6. MealAttendance
    mx, my_pos, mh = 100, 720, 200
    svg.append(f'<rect class="box" x="{mx}" y="{my_pos}" width="{bw}" height="{mh}"/>')
    svg.append(f'<line class="line" x1="{mx}" y1="{my_pos + 28}" x2="{mx + bw}" y2="{my_pos + 28}"/>')
    svg.append(f'<text class="title" x="{mx + bw/2}" y="{my_pos + 20}">MealAttendance</text>')
    m_attrs = ["id: int", "tenant_id: int", "date: date", "meal_type: string", "opted_in: boolean", "present: boolean", "diet: string"]
    ay = my_pos + 44
    for a in m_attrs:
        svg.append(f'<text class="body" x="{mx + 10}" y="{ay}">{a}</text>')
        ay += 15
    svg.append(f'<line class="line" x1="{mx}" y1="{ay + 4}" x2="{mx + bw}" y2="{ay + 4}"/>')
    meth_y = ay + 20
    for m in ["optInMeal()", "markAttendance()"]:
        svg.append(f'<text class="body" x="{mx + 10}" y="{meth_y}">{m}</text>')
        meth_y += 15

    # 7. VisitorPass
    vx, vy, vh = 575, 720, 200
    svg.append(f'<rect class="box" x="{vx}" y="{vy}" width="{bw}" height="{vh}"/>')
    svg.append(f'<line class="line" x1="{vx}" y1="{vy + 28}" x2="{vx + bw}" y2="{vy + 28}"/>')
    svg.append(f'<text class="title" x="{vx + bw/2}" y="{vy + 20}">VisitorPass</text>')
    v_attrs = ["id: int", "tenant_id: int", "visitor_name: string", "phone: string", "visit_date: date", "pass_code: string", "approval_status: string"]
    ay = vy + 44
    for a in v_attrs:
        svg.append(f'<text class="body" x="{vx + 10}" y="{ay}">{a}</text>')
        ay += 15
    svg.append(f'<line class="line" x1="{vx}" y1="{ay + 4}" x2="{vx + bw}" y2="{ay + 4}"/>')
    meth_y = ay + 20
    for m in ["generatePass()", "verifyQrCode()", "markCheckIn()"]:
        svg.append(f'<text class="body" x="{vx + 10}" y="{meth_y}">{m}</text>')
        meth_y += 15

    # 8. MaintenanceRequest
    cx, cy, ch = 1050, 720, 210
    svg.append(f'<rect class="box" x="{cx}" y="{cy}" width="{bw}" height="{ch}"/>')
    svg.append(f'<line class="line" x1="{cx}" y1="{cy + 28}" x2="{cx + bw}" y2="{cy + 28}"/>')
    svg.append(f'<text class="title" x="{cx + bw/2}" y="{cy + 20}">MaintenanceRequest</text>')
    c_attrs = ["id: int", "tenant_id: int", "room_id: int", "category: string", "description: string", "priority: string", "status: string", "assigned_to: int"]
    ay = cy + 44
    for a in c_attrs:
        svg.append(f'<text class="body" x="{cx + 10}" y="{ay}">{a}</text>')
        ay += 15
    svg.append(f'<line class="line" x1="{cx}" y1="{ay + 4}" x2="{cx + bw}" y2="{ay + 4}"/>')
    meth_y = ay + 20
    for m in ["logComplaint()", "assignStaff()", "resolveIssue()"]:
        svg.append(f'<text class="body" x="{cx + 10}" y="{meth_y}">{m}</text>')
        meth_y += 15

    # LINES & MULTIPLICITIES
    # User -> Tenant (Vertical)
    svg.append(f'<line class="line" x1="{ux + bw/2}" y1="{uy + uh}" x2="{tx + bw/2}" y2="{ty}"/>')
    svg.append(f'<text class="mult" x="{ux + bw/2 + 8}" y="{uy + uh + 18}">1</text>')
    svg.append(f'<text class="mult" x="{tx + bw/2 + 8}" y="{ty - 10}">0..1</text>')
    svg.append(f'<text class="assoc" x="{ux + bw/2 + 10}" y="{(uy + uh + ty)/2}">Identifies</text>')

    # User -> Employee (Horizontal)
    svg.append(f'<line class="line" x1="{ux + bw}" y1="{uy + 80}" x2="{ex}" y2="{ey + 80}"/>')
    svg.append(f'<text class="mult" x="{ux + bw + 10}" y="{uy + 72}">1</text>')
    svg.append(f'<text class="mult" x="{ex - 30}" y="{ey + 72}">0..1</text>')
    svg.append(f'<text class="assoc" x="{(ux + bw + ex)/2 - 20}" y="{uy + 75}">Employs</text>')

    # Room -> Tenant (Horizontal)
    svg.append(f'<line class="line" x1="{rx + bw}" y1="{ry + 90}" x2="{tx}" y2="{ty + 90}"/>')
    svg.append(f'<text class="mult" x="{rx + bw + 10}" y="{ry + 82}">1</text>')
    svg.append(f'<text class="mult" x="{tx - 20}" y="{ty + 82}">*</text>')
    svg.append(f'<text class="assoc" x="{(rx + bw + tx)/2 - 20}" y="{ry + 85}">Occupies</text>')

    # Tenant -> RentPayment (Horizontal)
    svg.append(f'<line class="line" x1="{tx + bw}" y1="{ty + 90}" x2="{px}" y2="{py + 90}"/>')
    svg.append(f'<text class="mult" x="{tx + bw + 10}" y="{ty + 82}">1</text>')
    svg.append(f'<text class="mult" x="{px - 20}" y="{py + 82}">*</text>')
    svg.append(f'<text class="assoc" x="{(tx + bw + px)/2 - 12}" y="{ty + 85}">Pays</text>')

    # Tenant -> VisitorPass (Vertical)
    svg.append(f'<line class="line" x1="{tx + bw/2}" y1="{ty + th}" x2="{vx + bw/2}" y2="{vy}"/>')
    svg.append(f'<text class="mult" x="{tx + bw/2 + 8}" y="{ty + th + 18}">1</text>')
    svg.append(f'<text class="mult" x="{vx + bw/2 + 8}" y="{vy - 10}">*</text>')
    svg.append(f'<text class="assoc" x="{tx + bw/2 + 10}" y="{(ty + th + vy)/2}">Requests</text>')

    # Tenant -> MealAttendance (Diagonal Left)
    svg.append(f'<line class="line" x1="{tx + 40}" y1="{ty + th}" x2="{mx + bw - 20}" y2="{my_pos}"/>')
    svg.append(f'<text class="mult" x="{tx + 20}" y="{ty + th + 18}">1</text>')
    svg.append(f'<text class="mult" x="{mx + bw - 10}" y="{my_pos - 10}">*</text>')
    svg.append(f'<text class="assoc" x="{(tx + 40 + mx + bw - 20)/2 - 25}" y="{(ty + th + my_pos)/2 - 10}">Opts-in</text>')

    # Tenant -> MaintenanceRequest (Diagonal Right)
    svg.append(f'<line class="line" x1="{tx + bw - 40}" y1="{ty + th}" x2="{cx + 20}" y2="{cy}"/>')
    svg.append(f'<text class="mult" x="{tx + bw - 30}" y="{ty + th + 18}">1</text>')
    svg.append(f'<text class="mult" x="{cx + 10}" y="{cy - 10}">*</text>')
    svg.append(f'<text class="assoc" x="{(tx + bw - 40 + cx + 20)/2 + 10}" y="{(ty + th + cy)/2 - 10}">Raises</text>')

    # Employee -> MaintenanceRequest (Vertical)
    svg.append(f'<line class="line" x1="{ex + bw/2}" y1="{ey + eh}" x2="{cx + bw/2}" y2="{cy}"/>')
    svg.append(f'<text class="mult" x="{ex + bw/2 + 8}" y="{ey + eh + 18}">1</text>')
    svg.append(f'<text class="mult" x="{cx + bw/2 + 8}" y="{cy - 10}">*</text>')
    svg.append(f'<text class="assoc" x="{ex + bw/2 + 10}" y="{(ey + eh + cy)/2}">Resolves</text>')

    svg.append('</svg>')
    return '\n'.join(svg)

def main():
    docs_dir = r"c:\Users\divya\-Roomzyy\docs"
    brain_dir = r"C:\Users\divya\.gemini\antigravity-ide\brain\f29ad74a-abd8-482e-973c-edd155f41144"
    os.makedirs(docs_dir, exist_ok=True)
    os.makedirs(brain_dir, exist_ok=True)
    
    print("Generating Single Unified UML Diagram Page...")
    img_page = build_portrait_single_uml_page()
    img_page.save(os.path.join(docs_dir, "Roomzyy_Single_UML_Diagram_Page.png"), "PNG", dpi=(300, 300))
    img_page.save(os.path.join(brain_dir, "Roomzyy_Single_UML_Diagram_Page.png"), "PNG", dpi=(300, 300))
    
    print("Generating Standalone Unified UML Diagram...")
    img_diag = build_single_uml_diagram_image()
    img_diag.save(os.path.join(docs_dir, "Roomzyy_Single_UML_Diagram.png"), "PNG", dpi=(300, 300))
    img_diag.save(os.path.join(brain_dir, "Roomzyy_Single_UML_Diagram.png"), "PNG", dpi=(300, 300))
    
    print("Generating SVG...")
    svg_content = generate_single_uml_svg()
    with open(os.path.join(docs_dir, "Roomzyy_Single_UML_Diagram.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    with open(os.path.join(brain_dir, "Roomzyy_Single_UML_Diagram.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    print("Unified UML Diagram generated successfully!")

if __name__ == '__main__':
    main()
