// Shared inter-module joint geometry (ADR-0001).
//
// Included by both the frame module and the joint coupon, so the coupon is a
// faithful test of the real joint rather than an approximation of it. If the
// coupon passes, the frame joint passes.
//
// STATUS: stub. Dimensions are placeholders until the joint is designed.

include <params.scad>

// --- joint parameters (move to rack/params.json once validated) ---
joint_tab_width    = 40;
joint_tab_height   = 12;
joint_tab_thick    = 6;
joint_shear_key_d  = 6;
joint_bolt_d       = 5.5;   // M5 clearance
joint_bolt_inset   = 15;    // from the tab end

// A female socket, cut from the top of a module.
module joint_socket() {
    // Tab slot, with print clearance so the parts actually assemble.
    translate([0, 0, -0.01])
        cube([joint_tab_width  + 2*print_clearance_general,
              joint_tab_thick  + 2*print_clearance_general,
              joint_tab_height + print_clearance_general], center = true);

    // Shear key hole: takes the load off the bolts.
    translate([0, 0, 0])
        rotate([90, 0, 0])
            cylinder(d = joint_shear_key_d + print_clearance_general,
                     h = joint_tab_thick + 4, center = true);

    // Bolt holes, slotted vertically so accumulated error has somewhere to go.
    for (x = [-joint_bolt_inset, joint_bolt_inset])
        translate([x, 0, 0])
            hull() {
                translate([0, 0, -2]) cylinder(d = joint_bolt_d, h = 4, center = true);
                translate([0, 0,  2]) cylinder(d = joint_bolt_d, h = 4, center = true);
            }
}

// A male tab, printed on the bottom of the module above.
module joint_tab() {
    cube([joint_tab_width, joint_tab_thick, joint_tab_height], center = true);

    translate([0, 0, 0])
        rotate([90, 0, 0])
            cylinder(d = joint_shear_key_d, h = joint_tab_thick + 2, center = true);

    for (x = [-joint_bolt_inset, joint_bolt_inset])
        translate([x, 0, 0])
            rotate([90, 0, 0])
                cylinder(d = joint_bolt_d, h = joint_tab_thick + 2, center = true);
}
