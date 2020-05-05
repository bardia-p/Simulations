%Graphing a cubic equation using desmos

setscreen ("graphics: 800,800")

var cx := 400
var cy := 400
var un : int := 40
var unn : real := un / 1.00
var sun : real := 40
var df : real := 1
var a : int := 1
var b : int := 1
var c : int := 1
var d : int := 1
var flag2 : int := 0

put "Simulating a cubic equation in the form of ax^3 + bx^2 + cx + d"
put "Move the graph by dragging it with the mouse. Zoom in with Up and zoom out with Down"
put "Enter the a value: "
get a
put "Enter the b value: "
get b
put "Enter the c value: "
get c
put "Enter the d value: "
get d

proc grids
    for i : cy .. 800 by un
	Draw.ThickLine (0, i, 800, i, 1, 30)
    end for
    for decreasing i : cy .. 0 by un
	Draw.ThickLine (0, i, 800, i, 1, 30)
    end for
    for j : cx .. 800 by un
	Draw.ThickLine (j, 0, j, 800, 1, 30)
    end for
    for decreasing j : cx .. 0 by un
	Draw.ThickLine (j, 0, j, 800, 1, 30)
    end for
end grids

proc axes (xd, yd : int)
    cx += xd
    cy += yd
    if un <= sun / 2 then
	df /= 2
	sun := sun / 2
    elsif un >= sun * 2 then
	df *= 2
	sun := sun * 2
    end if

    var count : real := 0
    count := cx
    var xx, yy : int
    loop
	xx := round (count)
	Draw.Text (realstr (round ((count - cx) / un * 100) / 100, 1), xx, cy - 20, Font.New ("arial:" + intstr (11 - 40 div un)), red)
	Draw.ThickLine (xx, cy - 10, xx, cy + 10, 1 + round (df / 1.5), black)
	exit when count >= 800 - un / df
	count += un / df
    end loop
    count := cx
    loop
	xx := round (count)
	Draw.Text (realstr (round ((count - cx) / un * 100) / 100, 1), xx, cy - 20, Font.New ("arial:" + intstr (11 - 40 div un)), red)
	Draw.ThickLine (xx, cy - 10, xx, cy + 10, 1 + round (df / 1.5), black)
	exit when count <= un / df
	count -= un / df
    end loop
    count := cy
    loop
	yy := round (count)
	Draw.Text (realstr (round ((count - cy) / un * 100) / 100, 1), cx - 40, yy, Font.New ("arial:" + intstr (11 - 40 div un)), red)
	Draw.ThickLine (cx - 10, yy, cx + 10, yy, 1 + round (df / 1.5), black)
	exit when count >= 800 - un / df
	count += un / df
    end loop
    count := cy
    loop
	yy := round (count)
	Draw.Text (realstr (round ((count - cy) / un * 100) / 100, 1), cx - 40, yy, Font.New ("arial:" + intstr (11 - 40 div un)), red)
	Draw.ThickLine (cx - 10, yy, cx + 10, yy, 1 + round (df / 1.5), black)
	exit when count <= un / df
	count -= un / df
    end loop
    Draw.ThickLine (cx, 0, cx, 800, 5, black)
    Draw.ThickLine (0, cy, 800, cy, 5, black)
end axes

function mapx (x : real, un : int) : int
    result round (cx + un * x)
end mapx

function mapy (y : real, un : int) : int
    result round (cy + un * y)
end mapy

function px (x : real, un : int) : real
    result (cx - x) / un
end px

function py (y : real, un : int) : real
    result (cy - y) / un
end py


proc plot_line (x1, y1, x2, y2 : real)
    Draw.ThickLine (mapx (x1, un), mapy (y1, un), mapx (x2, un), mapy (y2, un), 5, blue)
end plot_line

function f (x : real) : real
    result a * x ** 3 + b * x ** 2 + c * x + d
end f

proc plot_function
    for p : 0 .. 799
	if px (p, un) ~= 0 and px (p+1, un) ~= 0 then
	    plot_line (px (p, un), f (px (p, un)), px (p + 1, un), f (px (p + 1, un)))
	end if
    end for
end plot_function

setscreen ("graphics,800,800,offscreenonly")
Mouse.ButtonChoose ("multibutton")
var chars : array char of boolean
var x, y, xs, ys, xd, yd, button : int := 0
var sf : real := 1.00
var flag : int := 0
grids
axes (xd, yd)
plot_function
var press : int := 0
loop
    Mouse.Where (x, y, button)
    Input.KeyDown (chars)
    xs := x
    ys := y
    if flag = 1 then
	flag := 0
	Mouse.Where (x, y, button)
	xd := floor ((x - xs) / 5)
	yd := floor ((y - ys) / 5)
	delay (200)
	cls
	grids
	axes (xd, yd)
	plot_function
    end if
    if button = 1 then
	loop
	    Mouse.Where (x, y, button)
	    xd := floor ((x - xs) / 5)
	    yd := floor ((y - ys) / 5)
	    delay (100)
	    cls
	    grids
	    axes (xd, yd)
	    plot_function
	    flag := 1
	    exit when button ~= 1
	end loop
    end if
    if chars (KEY_UP_ARROW) and press = 0 then
	press := 1
	if un < 180 then
	    unn := un / sf
	    sf += 0.1
	    un := floor (unn * sf)
	end if
    elsif chars (KEY_DOWN_ARROW) and press = 0 then
	press := 1
	if un > 10 then
	    unn := un / sf
	    sf -= 0.1
	    un := floor (unn * sf)
	end if
    end if
    if press = 1 then
	delay (100)
	cls
	grids
	axes (xd, yd)
	plot_function
	View.Update ()
	xd := 0
	yd := 0
	if press = 1 then
	    press := 0
	end if
    end if
end loop
