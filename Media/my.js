$(function() 
  {
      $('#id_bundle').autocomplete('{% url bundle_lookup %}', {
	      dataType: 'json',
		  width: 500,
		  parse: function(data) {
		  return $.map(data, function(row) {
			  return { data:row, value:row[1], result:row[0] };
		      });
	      }
	  }).result(
		    function(e, data, value) {
			$("#id_bundle_pk").val(value);
		    }
		    );
  }
  );
