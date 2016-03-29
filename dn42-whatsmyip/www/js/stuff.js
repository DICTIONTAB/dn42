String.prototype.format = function()
{
	var str = this;
	for (var i = 0; i < arguments.length; i++)
	{
		var reg = new RegExp("\\{" + i + "\\}", "gm");
		str = str.replace(reg, arguments[i]);
	}
	return str;
}

$(document).ready(function() {
	var nowww = /^www\./
	var fqdn = location.hostname.replace(nowww,"")
	$.ajax({url: "http://ipv4.{0}/address.php".format(fqdn),
		timeout: 1500,
		success: function(address)
		{
			$("#v4 code").html(address);
			$("#v4").removeClass("loading");
		},
		error: function()
		{
			$("#v4 code").html("Not present");
			$("#v4").removeClass("loading").addClass("error");
		}
	});

	$.ajax({url: "http://ipv6.{0}/address.php".format(fqdn),
		timeout: 1500,
		success: function(address)
		{
			$("#v6 code").html(address);
			$("#v6").removeClass("loading");
		},
		error: function()
		{
			$("#v6 code").html("Not present");
			$("#v6").removeClass("loading").addClass("error");
		}
	});
});
