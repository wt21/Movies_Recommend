    var xhr = null;
    var xhrs = null;
	var flag =null;
	function createXMLHttpRequest() {
		var xmlhttp;
		if(window.XMLHttpRequest) {
			// code for IE7+, Firefox, Chrome, Opera, Safari 
			xmlhttp = new XMLHttpRequest();
		} else {
			// code for IE6, IE5
			xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
		}
		return xmlhttp;
	}

	function loadXML(url,f) {
		xhr = createXMLHttpRequest();
		flag = f;
		if(xhr != null) {
			xhr.onreadystatechange = state_Change;
			xhr.open("GET", url, true);
			xhr.send(null);
		}
	}
	function state_Change() {
		if(xhr.readyState == 4) { // 4 = "loaded" 
			if(xhr.status == 200) { // 200 = "OK" 
			   var txt = null;
			   var s = xhr.responseXML.documentElement.getElementsByTagName(flag);
			   var ss;
               ss = s[0].getElementsByTagName('car');
               txt = "<span>"+ss[0].firstChild.nodeValue+"</span>";
               for(var i=1; i<ss.length;i++){
            	 txt = txt + "&nbsp;&nbsp;&nbsp;&nbsp;<span>"+ss[i].firstChild.nodeValue+"</span>&nbsp;&nbsp;&nbsp;";
            	 document.getElementById("td_2_box2").innerHTML = txt;
               }
			}
		}
	}
	function loadXMLS(url,f) {
		alert("666");
		xhr = createXMLHttpRequest();
		flag = f;
		if(xhr != null) {
			xhr.onreadystatechange = state_Changes;
			xhr.open("GET", url, true);
			xhr.send(null);
		}
	}
	
	function state_Changes() {
		alert("555");
		if(xhr.readyState == 4) { // 4 = "loaded" 
			if(xhr.status == 200) { // 200 = "OK" 
			   var txt = null;
			   var s = xhr.responseXML.documentElement.getElementsByTagName(flag);
			   var ss;
               ss = s[0].getElementsByTagName('carstyle');
               txt = "<span>"+ss[0].firstChild.nodeValue+"</span>";
               for(var i=1; i<ss.length;i++){
            	 txt = txt + "&nbsp;&nbsp;&nbsp;&nbsp;<span>"+ss[i].firstChild.nodeValue+"</span>&nbsp;&nbsp;&nbsp;";
            	 document.getElementById("td_2_box3").innerHTML = txt;
               }
			}
		}
	}
	