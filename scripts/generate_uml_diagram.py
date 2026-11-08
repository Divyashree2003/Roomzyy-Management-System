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

def draw_uml_class(draw, x1, y1, width, title, attributes, methods, f_title, f_body, pad_y=14, pad_x=20):
    bbox_t = f_title.getbbox(title)
    h_title = (bbox_t[3] - bbox_t[1]) + pad_y * 2.2
    
    line_h_attr = []
    for attr in attributes:
        bb = f_body.getbbox(attr)
        line_h_attr.append(bb[3] - bb[1] + 8)
    h_attr = sum(line_h_attr) + pad_y * 1.5 if attributes else 0
    
    line_h_meth = []
    for meth in methods:
        bb = f_body.getbbox(meth)
        line_h_meth.append(bb[3] - bb[1] + 8)
    h_meth = sum(line_h_meth) + pad_y * 1.5 if methods else 0
    
    total_h = h_title + h_attr + h_meth
    x2 = x1 + width
    y2 = y1 + total_h
    
    # Outer rectangle
    draw.rectangle([x1, y1, x2, y2], fill='#ffffff', outline='#000000', width=2)
    
    # Title divider line
    draw.line([(x1, y1 + h_title), (x2, y1 + h_title)], fill='#000000', width=2)
    title_w = bbox_t[2] - bbox_t[0]
    draw.text((x1 + (width - title_w) / 2, y1 + pad_y - 2), title, font=f_title, fill='#000000')
    
    # Attributes
    curr_y = y1 + h_title + pad_y * 0.8
    for i, attr in enumerate(attributes):
        draw.text((x1 + pad_x, curr_y), attr, font=f_body, fill='#000000')
        curr_y += line_h_attr[i]
        
    # Methods divider line
    if methods:
        draw.line([(x1, y1 + h_title + h_attr), (x2, y1 + h_title + h_attr)], fill='#000000', width=2)
        curr_y = y1 + h_title + h_attr + pad_y * 0.8
        for i, meth in enumerate(methods):
            draw.text((x1 + pad_x, curr_y), meth, font=f_body, fill='#000000')
            curr_y += line_h_meth[i]
            
    return (x1, y1, x2, y2)

def build_tenant_uml_image():
    W = 2100
    H = 1750
    img = Image.new('RGB', (W, H), '#ffffff')
    draw = ImageDraw.Draw(img)
    
    f_title = get_font(32, bold=False, serif=True)
    f_body = get_font(26, bold=False, serif=True)
    f_label = get_font(27, italic=True, serif=True)
    f_mult = get_font(26, bold=False, serif=True)
    
    top_w = 560
    top_x1 = (W - top_w) / 2
    top_y1 = 60
    
    tenant_attrs = [
        "id: int",
        "name: string",
        "phone: string",
        "email: string",
        "password: string",
        "room_id: int",
        "id_proof_status: string"
    ]
    tenant_methods = [
        "login()",
        "profile()",
        "selectRoom()",
        "payDirectRent()",
        "requestVisitorPass()",
        "raiseMaintenance()",
        "viewHistory()"
    ]
    
    top_box = draw_uml_class(draw, top_x1, top_y1, top_w, "Tenant", tenant_attrs, tenant_methods, f_title, f_body)
    top_cx = (top_box[0] + top_box[2]) / 2
    top_bottom_y = top_box[3]
    
    bottom_y1 = 1000
    box_w = 530
    
    # Left: Rent Payment (Direct Payment - No Razorpay!)
    left_x1 = 70
    left_attrs = [
        "id: int",
        "month: string",
        "amount: float",
        "due_date: date",
        "payment_method: string",
        "status: string",
        "transaction_ref: string",
        "receipt_number: string"
    ]
    left_methods = [
        "makeDirectPayment()",
        "downloadReceiptPdf()"
    ]
    left_box = draw_uml_class(draw, left_x1, bottom_y1, box_w, "Rent Payment", left_attrs, left_methods, f_title, f_body)
    left_cx = (left_box[0] + left_box[2]) / 2
    
    # Center: Session Details
    center_x1 = (W - box_w) / 2
    center_attrs = [
        "id: int",
        "room_number: string",
        "room_type: string",
        "floor: string",
        "monthly_rent: float",
        "mess_opted: boolean",
        "diet_preference: string",
        "agreement_status: string"
    ]
    center_methods = [
        "viewRoomDetails()",
        "checkMessMenu()"
    ]
    center_box = draw_uml_class(draw, center_x1, bottom_y1 + 40, box_w, "Session Details", center_attrs, center_methods, f_title, f_body)
    center_cx = (center_box[0] + center_box[2]) / 2
    
    # Right: History
    right_x1 = W - box_w - 70
    right_attrs = [
        "id: int",
        "date: date",
        "event_type: string",
        "room_number: string",
        "amount_paid: float",
        "payment_method: string",
        "status: string",
        "receipt_number: string",
        "remarks: string"
    ]
    right_methods = []
    right_box = draw_uml_class(draw, right_x1, bottom_y1, box_w, "History", right_attrs, right_methods, f_title, f_body)
    right_cx = (right_box[0] + right_box[2]) / 2
    
    # Lines & Associations
    pt_top_l = (top_cx - 90, top_bottom_y)
    pt_bot_l = (left_cx + 70, left_box[1])
    draw.line([pt_top_l, pt_bot_l], fill='#000000', width=2)
    draw.text((pt_top_l[0] - 22, pt_top_l[1] + 10), "1", font=f_mult, fill='#000000')
    draw.text((pt_bot_l[0] - 26, pt_bot_l[1] - 38), "*", font=f_mult, fill='#000000')
    mid_l_x = (pt_top_l[0] + pt_bot_l[0]) / 2 - 14
    mid_l_y = (pt_top_l[1] + pt_bot_l[1]) / 2 - 14
    draw.text((mid_l_x, mid_l_y), "Manages", font=f_label, fill='#000000')
    
    pt_top_c = (top_cx, top_bottom_y)
    pt_bot_c = (center_cx, center_box[1])
    draw.line([pt_top_c, pt_bot_c], fill='#000000', width=2)
    draw.text((pt_top_c[0] - 22, pt_top_c[1] + 10), "1", font=f_mult, fill='#000000')
    draw.text((pt_bot_c[0] - 22, pt_bot_c[1] - 38), "*", font=f_mult, fill='#000000')
    mid_c_x = pt_top_c[0] + 10
    mid_c_y = (pt_top_c[1] + pt_bot_c[1]) / 2 - 14
    draw.text((mid_c_x, mid_c_y), "View", font=f_label, fill='#000000')
    
    pt_top_r = (top_cx + 90, top_bottom_y)
    pt_bot_r = (right_cx - 70, right_box[1])
    draw.line([pt_top_r, pt_bot_r], fill='#000000', width=2)
    draw.text((pt_top_r[0] + 12, pt_top_r[1] + 10), "1", font=f_mult, fill='#000000')
    draw.text((pt_bot_r[0] + 14, pt_bot_r[1] - 38), "*", font=f_mult, fill='#000000')
    mid_r_x = (pt_top_r[0] + pt_bot_r[0]) / 2 + 14
    mid_r_y = (pt_top_r[1] + pt_bot_r[1]) / 2 - 14
    draw.text((mid_r_x, mid_r_y), "View", font=f_label, fill='#000000')
    
    max_y = max(left_box[3], center_box[3], right_box[3]) + 40
    return img.crop((0, 0, W, max_y))

def build_admin_uml_image():
    W = 2100
    H = 1750
    img = Image.new('RGB', (W, H), '#ffffff')
    draw = ImageDraw.Draw(img)
    
    f_title = get_font(32, bold=False, serif=True)
    f_body = get_font(26, bold=False, serif=True)
    f_label = get_font(27, italic=True, serif=True)
    f_mult = get_font(26, bold=False, serif=True)
    
    top_w = 560
    top_x1 = (W - top_w) / 2
    top_y1 = 60
    
    admin_attrs = [
        "id: int",
        "name: string",
        "phone: string",
        "email: string",
        "role: string",
        "department: string",
        "status: string"
    ]
    admin_methods = [
        "login()",
        "manageRooms()",
        "manageTenants()",
        "manageStaff()",
        "verifyDirectPayments()",
        "generateReports()",
        "viewActivityLogs()"
    ]
    
    top_box = draw_uml_class(draw, top_x1, top_y1, top_w, "Admin", admin_attrs, admin_methods, f_title, f_body)
    top_cx = (top_box[0] + top_box[2]) / 2
    top_bottom_y = top_box[3]
    
    bottom_y1 = 1000
    box_w = 530
    
    # Left: Room & Bed Details
    left_x1 = 70
    left_attrs = [
        "id: int",
        "room_number: string",
        "room_type: string",
        "capacity: int",
        "occupied_beds: int",
        "monthly_rent: float",
        "status: string"
    ]
    left_methods = [
        "addRoom()",
        "allocateBed()",
        "vacateBed()"
    ]
    left_box = draw_uml_class(draw, left_x1, bottom_y1, box_w, "Room Allocation", left_attrs, left_methods, f_title, f_body)
    left_cx = (left_box[0] + left_box[2]) / 2
    
    # Center: Direct Payment Accounts (No Razorpay!)
    center_x1 = (W - box_w) / 2
    center_attrs = [
        "id: int",
        "tenant_id: int",
        "month: string",
        "amount: float",
        "payment_mode: string",
        "status: string",
        "receipt_number: string"
    ]
    center_methods = [
        "confirmPayment()",
        "exportLedgerPdf()"
    ]
    center_box = draw_uml_class(draw, center_x1, bottom_y1 + 40, box_w, "Direct Payments", center_attrs, center_methods, f_title, f_body)
    center_cx = (center_box[0] + center_box[2]) / 2
    
    # Right: Reports & Analytics
    right_x1 = W - box_w - 70
    right_attrs = [
        "id: int",
        "report_type: string",
        "period: string",
        "total_collection: float",
        "pending_dues: float",
        "occupancy_rate: float",
        "mess_expenses: float"
    ]
    right_methods = [
        "generateSummary()",
        "downloadPdfReport()"
    ]
    right_box = draw_uml_class(draw, right_x1, bottom_y1, box_w, "Reports & History", right_attrs, right_methods, f_title, f_body)
    right_cx = (right_box[0] + right_box[2]) / 2
    
    # Lines
    pt_top_l = (top_cx - 90, top_bottom_y)
    pt_bot_l = (left_cx + 70, left_box[1])
    draw.line([pt_top_l, pt_bot_l], fill='#000000', width=2)
    draw.text((pt_top_l[0] - 22, pt_top_l[1] + 10), "1", font=f_mult, fill='#000000')
    draw.text((pt_bot_l[0] - 26, pt_bot_l[1] - 38), "*", font=f_mult, fill='#000000')
    draw.text(((pt_top_l[0] + pt_bot_l[0]) / 2 - 14, (pt_top_l[1] + pt_bot_l[1]) / 2 - 14), "Manages", font=f_label, fill='#000000')
    
    pt_top_c = (top_cx, top_bottom_y)
    pt_bot_c = (center_cx, center_box[1])
    draw.line([pt_top_c, pt_bot_c], fill='#000000', width=2)
    draw.text((pt_top_c[0] - 22, pt_top_c[1] + 10), "1", font=f_mult, fill='#000000')
    draw.text((pt_bot_c[0] - 22, pt_bot_c[1] - 38), "*", font=f_mult, fill='#000000')
    draw.text((pt_top_c[0] + 10, (pt_top_c[1] + pt_bot_c[1]) / 2 - 14), "View", font=f_label, fill='#000000')
    
    pt_top_r = (top_cx + 90, top_bottom_y)
    pt_bot_r = (right_cx - 70, right_box[1])
    draw.line([pt_top_r, pt_bot_r], fill='#000000', width=2)
    draw.text((pt_top_r[0] + 12, pt_top_r[1] + 10), "1", font=f_mult, fill='#000000')
    draw.text((pt_bot_r[0] + 14, pt_bot_r[1] - 38), "*", font=f_mult, fill='#000000')
    draw.text(((pt_top_r[0] + pt_bot_r[0]) / 2 + 14, (pt_top_r[1] + pt_bot_r[1]) / 2 - 14), "View", font=f_label, fill='#000000')
    
    max_y = max(left_box[3], center_box[3], right_box[3]) + 40
    return img.crop((0, 0, W, max_y))

def build_portrait_uml_page(is_admin=False):
    PW = 2480
    PH = 3508
    page = Image.new('RGB', (PW, PH), '#ffffff')
    draw = ImageDraw.Draw(page)
    
    f_body_text = get_font(32, bold=False, serif=True)
    f_caption = get_font(36, bold=False, serif=True)
    f_footer = get_font(30, bold=True, serif=True)
    
    margin_x = 180
    margin_top = 180
    
    if is_admin:
        intro_lines = [
            "supervise overall paying-guest operations, allocate room inventory, monitor direct rent receipts,",
            "reconcile monthly cash and UPI transactions, and maintain audit logs to ensure high property",
            "accountability, accurate financial statements, and transparent management reporting."
        ]
        caption_text = "Fig 4.2.1.4 Admin UML Diagram"
    else:
        intro_lines = [
            "allow tenants to verify allotted room inventory, submit direct rent payments without third-party",
            "gateways, opt into daily mess meals, and maintain a detailed payment and stay history to ensure",
            "accurate records, transparent billing, and timely residential tracking."
        ]
        caption_text = "Fig 4.2.1.3 UML Diagram"
        
    curr_y = margin_top
    for line in intro_lines:
        draw.text((margin_x, curr_y), line, font=f_body_text, fill='#222222')
        curr_y += 46
        
    diag_img = build_admin_uml_image() if is_admin else build_tenant_uml_image()
    
    avail_w = PW - 2 * margin_x
    avail_h = PH - curr_y - 480
    scale = min(avail_w / diag_img.width, avail_h / diag_img.height) * 0.98
    new_w = int(diag_img.width * scale)
    new_h = int(diag_img.height * scale)
    
    diag_resized = diag_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    paste_x = int((PW - new_w) / 2)
    paste_y = int(curr_y + 40 + (avail_h - new_h) / 2)
    page.paste(diag_resized, (paste_x, paste_y))
    
    bbox_cap = f_caption.getbbox(caption_text)
    cap_w = bbox_cap[2] - bbox_cap[0]
    draw.text(((PW - cap_w) / 2, paste_y + new_h + 60), caption_text, font=f_caption, fill='#111111')
    
    line1_y = PH - 230
    line2_y = line1_y + 8
    draw.line([(margin_x, line1_y), (PW - margin_x, line1_y)], fill='#555555', width=4)
    draw.line([(margin_x, line2_y), (PW - margin_x, line2_y)], fill='#777777', width=2)
    
    draw.text((margin_x, line2_y + 22), "Department of MCA", font=f_footer, fill='#555555')
    page_txt = "Page | 46" if is_admin else "Page | 45"
    bbox_p = f_footer.getbbox(page_txt)
    pw = bbox_p[2] - bbox_p[0]
    draw.text(((PW - pw) / 2, line2_y + 22), page_txt, font=f_footer, fill='#555555')
    
    pim_txt = "PIM, Udupi"
    bbox_pim = f_footer.getbbox(pim_txt)
    pim_w = bbox_pim[2] - bbox_pim[0]
    draw.text((PW - margin_x - pim_w, line2_y + 22), pim_txt, font=f_footer, fill='#555555')
    
    return page

def main():
    docs_dir = r"c:\Users\divya\-Roomzyy\docs"
    brain_dir = r"C:\Users\divya\.gemini\antigravity-ide\brain\f29ad74a-abd8-482e-973c-edd155f41144"
    os.makedirs(docs_dir, exist_ok=True)
    os.makedirs(brain_dir, exist_ok=True)
    
    print("Generating Tenant Portrait UML Page...")
    img_tenant_page = build_portrait_uml_page(is_admin=False)
    img_tenant_page.save(os.path.join(docs_dir, "Roomzyy_UML_Diagram_Page.png"), "PNG", dpi=(300, 300))
    img_tenant_page.save(os.path.join(brain_dir, "Roomzyy_UML_Diagram_Page.png"), "PNG", dpi=(300, 300))
    
    print("Generating Standalone Tenant UML Diagram...")
    img_tenant_diag = build_tenant_uml_image()
    img_tenant_diag.save(os.path.join(docs_dir, "Roomzyy_UML_Diagram.png"), "PNG", dpi=(300, 300))
    img_tenant_diag.save(os.path.join(brain_dir, "Roomzyy_UML_Diagram.png"), "PNG", dpi=(300, 300))
    
    print("Generating Admin Portrait UML Page...")
    img_admin_page = build_portrait_uml_page(is_admin=True)
    img_admin_page.save(os.path.join(docs_dir, "Roomzyy_Admin_UML_Diagram_Page.png"), "PNG", dpi=(300, 300))
    img_admin_page.save(os.path.join(brain_dir, "Roomzyy_Admin_UML_Diagram_Page.png"), "PNG", dpi=(300, 300))
    
    print("All UML diagrams generated successfully!")

if __name__ == '__main__':
    main()
