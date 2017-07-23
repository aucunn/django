function keyenter(x)
{
	if(event.keyCode == 13)
	{
		if(x == 0)
			document.getElementById('pass').focus();
		else if(x == 1)
			document.getElementById('repass').focus();
		else if(x == 2)
			document.getElementById('name').focus();
	}
}

function submitkey()
{
	if(event.keyCode == 13)
		document.getElementById('account').submit();
}

function labelAction(x)
{
	if(document.getElementById(x).value.length>0)
		document.getElementById(x+"label").style.transform="scale(0.7) translateY(-60px)";
	else
		document.getElementById(x+"label").style.transform="scale(1) translateY(-25px)";
}
