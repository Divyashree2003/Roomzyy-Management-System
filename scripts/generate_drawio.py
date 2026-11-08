import os
import xml.etree.ElementTree as ET

def create_drawio_xml():
    mxfile = ET.Element('mxfile', host="app.diagrams.net", version="21.0.0")
    diagram = ET.SubElement(mxfile, 'diagram', name="Structure Chart", id="structure-chart")
    model = ET.SubElement(diagram, 'mxGraphModel', dx="1422", dy="794", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="1400", pageHeight="850", background="#ffffff", math="0", shadow="0")
    root = ET.SubElement(model, 'root')
    
    ET.SubElement(root, 'mxCell', id="0")
    ET.SubElement(root, 'mxCell', id="1", parent="0")
    
    cell_id = 2
    
    # Common styles
    STYLE_ROOT = "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=2.5;fontStyle=1;fontSize=14;fontFamily=Helvetica;"
    STYLE_L1 = "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontStyle=1;fontSize=12;fontFamily=Helvetica;"
    STYLE_L2 = "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontStyle=1;fontSize=11;fontFamily=Helvetica;"
    STYLE_LEAF = "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1.5;fontStyle=0;fontSize=11;fontFamily=Helvetica;"
    STYLE_EDGE = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.5;"

    def add_box(label, x, y, w, h, style):
        nonlocal cell_id
        cid = str(cell_id)
        cell_id += 1
        cell = ET.SubElement(root, 'mxCell', id=cid, value=label, style=style, vertex="1", parent="1")
        ET.SubElement(cell, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h), as_="geometry")
        return cid

    def add_edge(source_id, target_id):
        nonlocal cell_id
        cid = str(cell_id)
        cell_id += 1
        edge = ET.SubElement(root, 'mxCell', id=cid, style=STYLE_EDGE, edge="1", parent="1", source=source_id, target=target_id)
        ET.SubElement(edge, 'mxGeometry', relative="1", as_="geometry")
        return cid

    # Root Admin
    id_admin = add_box("Admin", 620, 40, 140, 45, STYLE_ROOT)
    
    # Level 1 Modules
    # 5 branches
    id_rep = add_box("Reports", 120, 150, 130, 45, STYLE_L1)
    id_att = add_box("Attendance<br>Management", 340, 150, 140, 45, STYLE_L1)
    id_usr = add_box("App Users", 560, 150, 130, 45, STYLE_L1)
    id_mst = add_box("Masters", 860, 150, 130, 45, STYLE_L1)
    id_mnt = add_box("Maintenance<br>Management", 1170, 150, 140, 45, STYLE_L1)
    
    for mid in [id_rep, id_att, id_usr, id_mst, id_mnt]:
        add_edge(id_admin, mid)
        
    # Branch 1: Reports
    id_daily = add_box("Daily Logs", 60, 250, 110, 40, STYLE_L2)
    id_month = add_box("Monthly", 190, 250, 110, 40, STYLE_L2)
    add_edge(id_rep, id_daily)
    add_edge(id_rep, id_month)
    
    id_def = add_box("Defaulters", 60, 340, 110, 36, STYLE_LEAF)
    id_occ = add_box("Occupancy", 190, 340, 110, 36, STYLE_LEAF)
    add_edge(id_daily, id_def)
    add_edge(id_month, id_occ)
    
    # Branch 2: Attendance Management
    id_mess = add_box("Mess Attendance", 280, 340, 120, 36, STYLE_LEAF)
    id_staff_att = add_box("Staff Attendance", 415, 340, 120, 36, STYLE_LEAF)
    add_edge(id_att, id_mess)
    add_edge(id_att, id_staff_att)
    
    # Branch 3: App Users
    id_u_ten = add_box("Tenants", 560 - 85, 340, 75, 36, STYLE_LEAF)
    id_u_stf = add_box("Staff", 560, 340, 75, 36, STYLE_LEAF)
    id_u_adm = add_box("Admin", 560 + 85, 340, 75, 36, STYLE_LEAF)
    add_edge(id_usr, id_u_ten)
    add_edge(id_usr, id_u_stf)
    add_edge(id_usr, id_u_adm)
    
    # Branch 4: Masters (Rooms, Tenants, Employees with Staggered CRUD)
    id_m_rooms = add_box("Rooms", 740, 250, 100, 40, STYLE_L2)
    id_m_tenants = add_box("Tenants", 875, 250, 100, 40, STYLE_L2)
    id_m_staff = add_box("Employees", 1010, 250, 100, 40, STYLE_L2)
    add_edge(id_mst, id_m_rooms)
    add_edge(id_mst, id_m_tenants)
    add_edge(id_mst, id_m_staff)
    
    # Rooms CRUD (Step 1, y = 340)
    for i, txt in enumerate(["Add", "Edit", "Delete"]):
        cid = add_box(txt, 740 - 75 + i * 75, 340, 65, 36, STYLE_LEAF)
        add_edge(id_m_rooms, cid)
        
    # Tenants CRUD (Step 2, y = 430)
    for i, txt in enumerate(["Add", "Edit", "Delete"]):
        cid = add_box(txt, 875 - 75 + i * 75, 430, 65, 36, STYLE_LEAF)
        add_edge(id_m_tenants, cid)
        
    # Employees CRUD (Step 3, y = 520)
    for i, txt in enumerate(["Add", "Edit", "Delete"]):
        cid = add_box(txt, 1010 - 75 + i * 75, 520, 65, 36, STYLE_LEAF)
        add_edge(id_m_staff, cid)
        
    # Branch 5: Maintenance Management (y = 340)
    for i, txt in enumerate(["Add", "Edit", "Delete"]):
        cid = add_box(txt, 1240 - 75 + i * 75, 340, 65, 36, STYLE_LEAF)
        add_edge(id_mnt, cid)
        
    return ET.tostring(mxfile, encoding="utf-8", method="xml").decode("utf-8")

if __name__ == '__main__':
    xml_content = create_drawio_xml()
    out_path = r"c:\Users\divya\-Roomzyy\docs\Roomzyy_Structure_Chart.drawio"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print("Generated Roomzyy_Structure_Chart.drawio successfully!")
