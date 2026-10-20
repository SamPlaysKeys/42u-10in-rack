// Standard rack panel outline, shared by every panel and shelf.
//
// Guarantees that every panel is the same silhouette with the same hole
// positions, so a fit problem is a fit problem in one place rather than seven.
//
// STATUS: stub. Hole geometry depends on ADR-0002 (cage nuts vs printed threads).

include <params.scad>

// If params.scad is missing, OpenSCAD resolves every spec variable to undef and
// silently renders a 1 mm cube. Fail loudly instead.
assert(width_nominal_panel_width != undef, "params.scad did not load - run scripts/params_to_scad.py");

panel_thickness = 4;

// The correct 1U panel height, not the full 44.45 mm U. The 0.8 mm difference
// is split top and bottom so stacked panels cannot foul each other.
module panel_outline(u = 1) {
    h = u * rack_unit_u_height - (rack_unit_u_height - rack_unit_panel_height_1u) * u;
    square([width_nominal_panel_width, h], center = true);
}

// One mounting hole, positioned at the spec's 236.525 mm centres.
module mount_hole() {
    if (rail_hole_type == "square_cage_nut") {
        square([rail_square_hole, rail_square_hole], center = true);
    } else {
        circle(d = rail_round_hole_m6, $fn = 32);
    }
}

module panel_2d(u = 1) {
    difference() {
        panel_outline(u);
        for (x = [-width_hole_centres/2, width_hole_centres/2])
            translate([x, 0]) mount_hole();
    }
}

module panel(u = 1) {
    linear_extrude(height = panel_thickness, center = true)
        panel_2d(u);
}
