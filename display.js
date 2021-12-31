var data = "{{dataTeam}}";
data = JSON.parse(data.replace(/&quot;/g, '"'));

var data_size = Object.keys(data);

//add one name into its own div within teamMember
for (var i = 0; i < data_size.length; i++) {
var member_div = document.createElement("div");
member_div.classList.add("teamMember");
var name_para = document.createElement("b");
//name_para.classList.add("nameText");
	    var member_data = document.createElement("div");
	    member_data.classList.add("memberData");

user_admin = true;
var member_name = document.createTextNode(data[i].first_name + " " + data[i].last_name); 
name_para.appendChild(member_name);
if (user_admin) {
    var admin_text = document.createTextNode(" (admin)");
    name_para.appendChild(admin_text);
}
var phone_para = document.createElement("p");
var phone_number = document.createTextNode("999-999-999"); 
phone_para.appendChild(phone_number);
var email = document.createTextNode(data[i].email);

member_data.appendChild(name_para);
member_data.appendChild(phone_para);
member_data.appendChild(email);

member_image = document.createElement("img");
image_url = "employees/images/" + data[i].profile_picture;
member_image.src = "{% static 'employees/images/profile.webp' %}";
member_image.classList.add("profilePicture");

member_div.appendChild(member_image);
    member_div.appendChild(member_data);






var current_div = document.getElementById("end");
var inner_div = document.getElementById("list");

inner_div.appendChild(member_div);
}