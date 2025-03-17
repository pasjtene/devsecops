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
    updateComment();
    //updateComment();
    /**
     * Easy selector helper function
     */
   
   function addNewComments(comment,deleteURL, updateURL) {
    const commentsList = document.getElementById('commentsList');
    var uUrl = updateURL.replace("0",comment.comment_id);
    var dUrl = deleteURL.replace("0",comment.comment_id);

    const comentItem = `
    <div class="card mb-3" id="${comment.comment_id}">
        <div class="card-body">
            <h5 class="card-title">${comment.created_by}</h5>
            <p class="card-text" id="text${comment.comment_id}"> ${comment.comment_text}</p>
            <small class="text-muted">${new Date(comment.created_date).toLocaleString()} </small>

            <!-- Update, and Delete Links -->
                <span class="comment-link update-btn" 
                data-comment-id="${comment.comment_id}" data-update-url="${uUrl}">Update</span>
                <span data-delete-url="${dUrl}" class="comment-link delete-btn">Delete</span>
        </div>
    </div>`;

    commentsList.innerHTML =  comentItem + commentsList.innerHTML;
    updateComment();
   }

   function updateComment(){
     // Handle update comment modal
     $('.update-btn').click(function(e) {
        e.preventDefault();
        var commentId = $(this).data('comment-id');
        var updateUrl = $(this).data('update-url');
        //var updateUrl = "{% url 'update_comment' 0 %}".replace("0", commentId);
        var updtext = $(this).siblings('.card-text').text();
        $('#update-comment-text').val(updtext);

            $('#update-comment-form').attr('action', updateUrl);
            $('#updateCommentModal').modal('show');

    });

     // Handle delete comment modal
     $('.delete-btn').click(function(e) {
        e.preventDefault();
        var commentId = $(this).data('comment-id');
        var deleteUrl = $(this).data('delete-url');
        //var updateUrl = "{% url 'update_comment' 0 %}".replace("0", commentId);
        var deltext = $(this).siblings('.card-text').text();
        $('#delete-comment-text').val(deltext);

            $('#delete-comment-form').attr('action', deleteUrl);
            $('#deleteCommentModal').modal('show');

    });

    // Handle delete comment via AJAX
    $('#delete-comment-form').submit(function(e) {
        e.preventDefault();
        var form = $(this);
        var durl = form.attr('action');
        var commentText = $('#delete-comment-text').val();
        $('#deleteCommentModal').modal('hide');

        $.ajax({
            url: durl,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'comment_text': commentText
            },
            success: function(response) {
                if (response.success) {
                    console.log(response);
                    
                    $('#'+response.comment_id).remove();
                    $('.ajax-alert').show()
                    $('.alert-dismissible').show()
                    $('#ajax-alert-message').text("Comment deleted successfuly ");
                  
                } else {
                    alert('Error Deleting comment.');
                }
            },
            error: function(response) {
                alert('Error deleting comment.');
            }
        });
    });


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
                        addNewComments(response,deleteURL,updateURL); // Refresh the comments list
                      
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