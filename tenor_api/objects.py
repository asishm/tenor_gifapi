from datetime import datetime

class Media:
    def __init__(self, preview, url, **kwargs):
        """
        attributes:

        preview: a url to a preview image of the media source
        url: a url to the media source
        """
        self.preview = preview
        self.url = url
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return "preview url: {}\nurl: {}".format(self.preview, self.url)

# class Composite:
#     def __init__(self, video=None, preview=None):
#         """
#         attributes:

#         video: for GIF Stories,
#                a composite video containing all of the individual GIFs
#                in this object in MP4 format, otherwise null.
#         preview: preview url
#         """
#         self.video = video,
#         self.preview = preview

#     def __repr__(self):
#         return "video: {self.video}\npreview: {self.preview}".format(self=self)

class MediaCollection:
    def __init__(self, gif, mp4, tinygif, webm, **kwargs):
        """
        attributes:

        gif: Media object: a large-format GIF, good for desktop use,
        mp4: Media object: a video version of the GIF
        tinygif: Media object: a small-format GIF, good for mobile use
        webm: Media object: a video version of the GIF
        """
        self.gif = Media(**gif)
        self.mp4 = Media(**mp4)
        self.tinygif = Media(**tinygif)
        self.webm = Media(**webm)
        for k,v in kwargs.items():
            setattr(self, k, Media(**v))

    def __repr__(self):
        _gif = "gif:\n" + str(self.gif)
        _mp4 = "mp4:\n" + str(self.mp4)
        _tinygif = "tinygif:\n" + str(self.tinygif)
        _webm = "webm:\n" + str(self.webm)
        return "\n".join([_gif, _mp4, _tinygif, _webm])

class Result:
    def __init__(self, composite, created, hasaudio, id, media, tags, title, url, **kwargs):
        """
        attributes:

        composite: Composite:
        created: timestamp: a unix timestamp representing when this post was created.
        hasaudio: bool: true if this post contains audio (only video formats support audio
                        the gif image file format can not contain audio information).
        id: string: Tenor result identifier
        media: MediaCollection: a collection of Media objects
        tags: list: an array of tags for the post
        title: string: the title of the post
        url: string: a short URL to view the post on tenor.co
        """
        # self.composite = Composite(**composite)
        self.composite = composite
        self.created = datetime.utcfromtimestamp(created)
        self.hasaudio = hasaudio
        self.id = id
        self.media = MediaCollection(**media[0])
        self.tags = tags
        self.title = title
        self.url = url
        for key, val in kwargs.items():
            setattr(self, key, val)

class Response:
    def __init__(self, next, results):
        """
        attributes:

        next: string: a position identifier to use with the next API query to retrieve
                      the next set of results, or null if there are no further results.
        results: list: an array of Result objects, containing GIF and video data
        """
        self.next = next
        self.results = [Result(**result) for result in results]
