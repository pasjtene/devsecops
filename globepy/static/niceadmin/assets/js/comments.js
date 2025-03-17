/**
* Created: 2025/03/17
* 
* Updated: Apr 20 2025 with Bootstrap v5.3.3
* Author: Pascal Tene
* License: To be confirmed (Private)
*/

(function() {
    "use strict";
    $(document).ready(function() {
    //viewRequirementDetails();
    addCommentJson();
    /**
     * Easy selector helper function
     */
   
   function addComments(comment,deleteURL, updateURL) {
    const commentsList = document.getElementById('commentsList');
    const comentItem = `
    <div class="card mb-3" id=" ${comment.comment_id} ">
        <div class="card-body">
            <h5 class="card-title">${comment.created_by}</h5>
            <p class="card-text" id="text${comment.comment_id}"> ${comment.comment_text}</p>
            <small class="text-muted">${comment.created_date} | ${new Date(comment.created_date).toLocaleString()} </small>

            <!-- Reply, Update, and Delete Links -->
            <span href="#" class="comment-link reply-btn">Reply</span>
            
                <a href="#" class="comment-link update-btn" data-comment-id="${comment.comment_id}" data-update-url="${updateURL}">Update</a>
                <a href="#" data-delete-url="${deleteURL}" class="comment-link delete-btn">Delete</a>
        </div>
    </div>`;

    commentsList.innerHTML =  comentItem + commentsList.innerHTML;
   }

    function addCommentJson() {
       
        // Submit a new comment
        
        
        $('#comment-form-form').submit(function(e) {
            e.preventDefault();
            var form = $(this);
            var url = form.attr('action');
            var deleteURL = $(this).data('delete-url');
            var updateURL = $(this).data('update-url');

            var commentText = $('#comment-text').val();
            //$('#deleteCommentModal').modal('hide');

            $.ajax({
                url: url,
                type: 'POST',
                data: {
                    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                    'comment_text': commentText
                },
                success: function(response) {
                    if (response.success) {
                        
                       // $('#'+response.comment_id).remove();
                        //$('.ajax-alert').show()
                        //$('.alert-dismissible').show()
                        $('#ajax-alert-message').text("Comment added successfuly ");
                        console.log(response)
                        addComments(response,deleteURL,updateURL); // Refresh the comments list
                      
                    } else {
                        alert('Error updating comment.');
                    }
                },
                error: function(response) {
                    alert('Error updating comment.');
                }
            });
        });
        

    }

});

  })();